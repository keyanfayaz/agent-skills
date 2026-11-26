---
name: review-change
description: Review a code change or pull request against request intent, acceptance criteria, project conventions, and regression risk. Use for requested code reviews and ticket-alignment checks.
---

# Review change

Ground findings in the requested outcome and the actual diff.

## Establish the contract

Read the request, acceptance criteria, non-goals, and applicable AGENTS files. Identify the exact diff and base under review. State any inferred contract when the ticket or criteria are missing.

## Inspect

Prioritize incorrect behavior, regressions, data integrity, security, compatibility, and missing verification of changed behavior. Report style only when it causes a concrete maintainability or correctness problem beyond existing automation.

Each finding includes:

- Severity, short title, and exact location when available.
- The condition that triggers it and its concrete impact.
- A safe direction for a fix.

Avoid speculative findings without a plausible trigger and impact.

## Verify and hand off

Run relevant existing checks. For affected application flows, use `verify-app` if available, passing the criteria and project verification profile. Report missing runtime evidence explicitly.

Deliver critical issues first, then other findings in severity order, followed by a concise ticket-alignment assessment, verification evidence, and material remaining gaps. Say plainly when no findings were found.
