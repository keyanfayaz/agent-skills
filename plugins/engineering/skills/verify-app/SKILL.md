---
name: verify-app
description: Verify a website or application against acceptance criteria using relevant checks, functional flows, and screenshot evidence. Use after app changes or for requested functional QA.
---

# Verify application behavior

Match the depth of verification to the changed behavior and its risk.

## Establish the contract

Read the request, applicable AGENTS files, project verification profile, and existing run/test instructions. Use the supplied environment and identify it in the report.

Make a compact verification matrix: criterion or risk, prerequisite, expected result, actual result, status, and evidence.

## Execute

1. Run the smallest relevant static checks and automated tests using the project's commands and package manager. Broaden when failures or unresolved risk justify it.
2. For application behavior, traverse affected journeys in the real runtime, including meaningful failure, empty, and boundary states. Use the project's test fixtures and accounts when provided.
3. For visual behavior, inspect relevant responsive layouts and interactions. Capture meaningful checkpoints and failures in a run-specific evidence folder, separate from product assets.
4. Record relevant console, network, server, redirect, or crash evidence beside the failing criterion.
5. Compare the criteria, executed checks, and produced artifacts. Investigate mismatches.

Compilation is evidence of compilation. Only executed runtime tests support a runtime-test result. Distinguish product failures from unavailable environments; record blocked checks with the exact missing prerequisite.

## Deliver

Return `Pass`, `Pass with gaps`, `Fail`, or `Blocked`, followed by the compact matrix, commands and results, relevant evidence links, and remaining coverage gaps. Count only checks actually performed. An unavailable check is blocked, not passed.
