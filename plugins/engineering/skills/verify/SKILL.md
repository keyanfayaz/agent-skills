---
name: verify
description: Verify a feature against a specific Linear ticket. Run checks on the target build and report evidence for each acceptance criterion.
---

# Verify a ticket

1. Resolve the supplied Linear issue ID or URL and read the ticket. If a number matches more than one issue, ask which one. If Linear is unavailable, ask for the ticket text. Use its acceptance criteria, or the observable outcomes in its description. Ask for clarification where the expected behavior is unclear.
2. Identify the build or commit under test. Read the project's verification instructions for commands, fixtures, accounts, and supported platforms. Map each criterion to a check that could reveal a failure. Include error paths when the ticket calls for them.
3. Run the checks. Exercise user-facing behavior in the app or through an existing functional test that covers the same flow. Record the observed result and useful evidence, such as a test name, screenshot, or log excerpt. A successful compile alone leaves runtime behavior unverified.
4. Report the ticket, build, and one result per criterion. Use **Pass** when the observation matches the expectation, **Fail** for a mismatch, and **Blocked** when a prerequisite prevented the check. Give reproduction steps for a failure or the missing prerequisite for a blocked check. Report the whole ticket as passing only when every criterion passes.
