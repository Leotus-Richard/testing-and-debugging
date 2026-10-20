---
name: testing-and-debugging
description: Implement requested behavior test-first, diagnose reproducible bugs, or prove a regression fix with observed red/green evidence. Use for feature TDD and evidence-driven debugging; do not force new tests or harnesses for unrelated low-impact edits.
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
than private calls. Consult the bundled [test](references/source/tdd/references/upstream/tests.md)
and [mocking](references/source/tdd/references/upstream/mocking.md) guidance as needed.

Rerun the focused test and original scenario; run broader relevant checks only
when the change or remaining uncertainty warrants them. Remove temporary tagged
instrumentation while preserving useful reproduction evidence. If a reliable
automated test is impractical, report the closest executable check and its limits.
Do not call a check passed when it was only drafted, blocked, or not executed.

## Deliver evidence

Report the trigger, accepted explanation or open hypotheses, authorized change,
actual commands/results, and remaining limitations. Keep a diagnosis-only request
read-only apart from authorized scratch evidence. Commit or tracker actions are
optional integrations governed by the request, not prerequisites for testing.

The [reference index](references/README.md) retains full source workflows and
optional root-cause, behavior-testing, and proof principles. Its helper shell
template is archived source; adapt and review it for the actual OS/target before
separately authorized use. Historical model, host, identity, sibling-loading,
and local-only rules do not expand or replace the current task scope.
