---
name: testing-and-debugging
description: Implement requested behavior test-first, diagnose reproducible bugs, or prove a regression fix with observed red/green evidence. When test quality is in doubt, kill surviving mutants with mutation testing. In TypeScript, report errors as template-literal feature:error codes. Use for feature TDD and evidence-driven debugging; do not force new tests or harnesses for unrelated low-impact edits.
---

# Testing and debugging

Build a tight feedback loop around the real behavior. Work with existing project
tools and the authorized target; no tracker, commit plugin, or particular host is required.

## Select the task

- For a **feature**, identify intended behavior, an existing public seam, and an
  independently known expected result. Write one meaningful behavior test, run it,
  and verify that it fails for the intended reason. Implement enough to pass, run it
  again, then continue one vertical slice at a time.
- For a **reported bug**, reproduce the real trigger before editing. Reduce the
  case without removing its defining conditions. Compare a few falsifiable hypotheses
  and choose probes that distinguish them; do not prescribe a hypothesis count.
- For a **regression fix**, choose the cheapest existing seam that reaches the actual
  failure. Observe the check fail before the fix and pass after it. A superficial
  assertion that misses the triggering path is not regression proof.

## Investigate efficiently

Inspect affected code, relevant domain rules, diagnostics, and change history when
available. Prefer executable tests, request scripts, CLI fixtures, browser checks,
replays, or small harnesses that reach the issue. Use human observation when the
behavior cannot be measured directly, with a clear bounded reproduction procedure.
Redact secrets from captured evidence and avoid disrupting unrelated instances.

State each important hypothesis's predicted observation. Change one relevant
variable at a time and distinguish observations from inferred causes. Measure
performance against a stated baseline and comparable conditions. Stop a probe
when it cannot distinguish explanations or exceeds the task's useful budget.

## Make and verify the requested change

Fix the shared cause when evidence supports it. Preserve security and boundary
validation; do not suppress the symptom through broad catches or weakened checks.
Mock external boundaries when necessary while testing public behavior rather
than private calls. Consult the bundled [test](references/r/029.md)
and [mocking](references/r/028.md) guidance as needed.

Rerun the focused test and original scenario; run broader relevant checks only
when the change or remaining uncertainty warrants them. Remove temporary tagged
instrumentation while preserving useful reproduction evidence. If a reliable
automated test is impractical, report the closest executable check and its limits.
Do not call a check passed when it was only drafted, blocked, or not executed.

When TypeScript reports an error, type that report as a template literal of a
feature union and an error-type union, joined by a colon. `reportError` accepts
only those codes, so autocomplete lists each pair and a free string does not
type-check. Adding an error type makes it reportable on every feature without
writing each pair by hand. Follow [template literal error codes](references/r/031.md).
Keep that template literal as the only error-code type. Use it in TypeScript;
leave other languages on their existing error-reporting style.

## Probe weak tests with mutation testing

When a passing suite's quality is in doubt, especially tests an agent wrote,
run mutation testing. Use the project's mutation tool when it has one. The
TypeScript example is Stryker.js; other languages have their own tools. Leave
the mutator out of an unrelated low-impact edit.

The mutator changes source, then reruns the tests. One mutation is a JavaScript
string replaced with an empty string. A mutation the tests still pass is a
surviving mutant and has to be killed. Kill it with a test that fails on that
mutation and passes on the original source, so the test catches a potential bug.
A killed mutant is one the suite already fails. A no-coverage mutant was never
executed, so it is not evidence the behavior is tested. Read
[mutation testing](references/r/030.md) before treating the report as done.

## Deliver evidence

Report the trigger, accepted explanation or open hypotheses, authorized change,
actual commands/results, and remaining limitations. If mutation testing ran,
include killed, survived, and no-coverage results and which survivors were
killed. If an error report changed, name the feature and error-type members.
Keep a diagnosis-only request read-only apart from authorized scratch evidence.
Commit or tracker actions are optional integrations governed by the request,
not prerequisites for testing.

The [reference index](references/README.md) lists the mutation-testing and
error-code guidance above, plus full source workflows and optional root-cause,
behavior-testing, and proof principles. Its helper shell
template is archived source; adapt and review it for the actual OS/target before
separately authorized use. Historical model, host, identity, sibling-loading,
and local-only rules do not expand or replace the current task scope.
