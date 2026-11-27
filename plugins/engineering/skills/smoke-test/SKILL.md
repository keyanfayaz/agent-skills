---
name: smoke-test
description: Run an app's core user flows on a specified build and report which work. Use for a quick build, deployment, or release check. No ticket is required.
---

# Smoke-test a build

1. Identify the target build and environment. Read the project's smoke suite, verification profile, or documented core journeys. If none are listed, use the project's getting-started flow and primary user action. Ask which flows matter if the project gives no clear starting point.
2. Run the existing smoke suite on that build, or walk the flows in the running app. Use the project's test accounts and fixtures when needed. For each flow, check the user-visible result. For example, if the main task is saving a draft, reopen the saved draft and check its contents.
3. If one flow fails, continue with independent flows. Mark a dependent flow **Blocked** when you cannot reach it. A successful build, health response, or page load covers only that step.
4. Report the build and environment, then one short line per flow: **Pass**, **Fail**, or **Blocked**, with the observed result. For failures, include the shortest reproduction or relevant evidence. For blocked flows, name the missing prerequisite.
