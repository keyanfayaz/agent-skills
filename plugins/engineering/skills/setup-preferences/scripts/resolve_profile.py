#!/usr/bin/env python3
"""Validate and merge the bundled preference format; print JSON without writes."""

import argparse
from copy import deepcopy
import json
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"


def validate(value, schema):
    """Validate the types and constraints used by the bundled profile schema."""
    types = {"object": dict, "array": list, "string": str, "integer": int, "boolean": bool}
    if type(value) is not types[schema["type"]]:
        raise ValueError("Wrong preference type")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError("Unsupported preference value or version")
    if type(value) is dict:
        properties = schema["properties"]
        if set(value) - properties.keys() or set(schema.get("required", [])) - value.keys():
            raise ValueError("Unknown or missing preference field")
        for key, item in value.items():
            validate(item, properties[key])
    elif type(value) is list:
        for item in value:
            validate(item, schema["items"])
    elif type(value) is int:
        if value < schema.get("minimum", value) or value > schema.get("maximum", value):
            raise ValueError("Preference outside supported range")


def merge(base, layer):
    """Merge objects recursively; supplied arrays and scalar values replace."""
    result = deepcopy(base)
    for key, value in layer.items():
        result[key] = merge(result.get(key, {}), value) if type(value) is dict else deepcopy(value)
    return result


def resolve(*layers):
    """Return defaults overlaid with validated preference layers in order."""
    schema = json.loads((ASSETS / "profile.schema.json").read_text())
    result = json.loads((ASSETS / "defaults.json").read_text())
    validate(result, schema)
    for layer in layers:
        validate(layer, schema)
        result = merge(result, layer)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=Path.home() / ".config/agent-skills/profile.json")
    parser.add_argument("--project", type=Path)
    parser.add_argument("--override", help="JSON preference layer for an explicit request")
    args = parser.parse_args()
    try:
        layers = []
        if args.profile.exists():
            layers.append(json.loads(args.profile.read_text()))
        elif args.profile != Path.home() / ".config/agent-skills/profile.json":
            raise ValueError("Selected profile does not exist")
        if args.project is not None:
            layers.append(json.loads(args.project.read_text()))
        if args.override is not None:
            layers.append(json.loads(args.override))
        print(json.dumps(resolve(*layers), indent=2))
    except (OSError, ValueError):
        parser.error("Invalid preferences; check the selected files against profile.schema.json")


if __name__ == "__main__":
    main()
