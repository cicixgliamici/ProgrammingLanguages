# Editorial Guide

This guide keeps lessons consistent, reviewable, and useful to readers who are
studying independently.

## Language and audience

Use English for new or substantially revised code, comments, filenames,
documentation, commit messages, and contribution discussions. Existing Italian
material may be translated incrementally without blocking unrelated
improvements. Write for a motivated learner who knows the stated prerequisites
but has not yet learned the lesson's central concept.

Prefer precise, direct language. Define specialist terms when they first
appear, and distinguish facts about a language from conventions or opinions.

## Lesson structure

Every substantial learning track should document:

1. its purpose and prerequisites;
2. an ordered lesson index;
3. setup and execution commands;
4. expected outcomes;
5. exercises or verification;
6. common mistakes;
7. authoritative further reading.

A source lesson should focus on one main idea. If its title requires “and” more
than once, consider splitting it.

## Code conventions

- Prefer short functions and descriptive names.
- Keep examples small enough to understand without hidden context.
- Explain decisions, invariants, ownership, trade-offs, or surprising behavior
  in comments.
- Do not add comments that only repeat the next line of code.
- Show error handling when failure is part of the concept being taught.
- Use deterministic data and seeded random generators where reproducibility
  matters.
- Add tests for reusable behavior and assertions for important lesson results.

Follow the standard formatter and naming conventions of the language. A track
may document a stricter convention in its own README.

## Naming and ordering

Within an existing track, preserve its current numbering until a deliberate
migration is approved. New tracks should use two-digit numeric prefixes and
lowercase descriptive names where the language permits it, for example:

```text
00_introduction.ext
01_types_and_values.ext
02_control_flow.ext
```

Do not encode temporary status such as `new`, `final`, or `fixed` in filenames.

## Dependencies and portability

Use the standard library unless an external dependency is central to the
lesson. Pin toolchain or dependency versions where practical, document how to
install them, and never commit machine-specific absolute paths.

Commands should work from the repository root unless the documentation clearly
states another working directory.

## Status and maintenance

Use the following status vocabulary consistently:

| Status | Meaning |
| --- | --- |
| Planned | A roadmap exists, but no executable lesson is available. |
| Draft | Useful material exists, but the learning path is incomplete. |
| Usable | The section has instructions, executable material, and exercises. |
| Verified | The material is automatically built or tested in CI. |
| Complete | The defined learning objectives and final project are present. |

Update the track index and `PROGRESS.md` in the same change as a new lesson.
Never present planned material as implemented.

## Sources and originality

Prefer official language documentation, specifications, and original examples.
Link to sources for factual or version-specific claims. Do not copy tutorial
text or exercises unless their license permits redistribution and attribution
is included.
