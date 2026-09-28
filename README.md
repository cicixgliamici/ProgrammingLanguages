# Programming Languages Reference & Practice

[![Verify learning examples](https://github.com/cicixgliamici/ProgrammingLanguages/actions/workflows/verify.yml/badge.svg)](https://github.com/cicixgliamici/ProgrammingLanguages/actions/workflows/verify.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](./CONTRIBUTING.md)

A curated, executable learning repository for studying programming languages,
programming paradigms, formal methods, and selected development ecosystems.

The project favors clear explanations, small examples, deliberate practice, and
reproducible verification over encyclopedic coverage. It is useful for guided
study, revision, interview preparation, and comparing how different languages
express the same ideas.

## Choose a learning track

### Language foundations

| Track | Current focus | Start here |
| --- | --- | --- |
| C | Memory, data structures, and algorithms | [C learning path](./C/README.md) |
| Java | Syntax, OOP, arrays, exceptions, and testing | [Java learning path](./Java/README.md) |
| Python | Core language, numerical computing, and applications | [Python learning path](./Python/README.md) |
| Scala | Functional and object-oriented programming with Scala 3 | [Scala learning path](./Scala/README.md) |

### Programming paradigms

The language tracks introduce imperative, object-oriented, and functional
programming in context. Cross-language comparison lessons are planned so that
the same problem can be studied through more than one paradigm.

### Formal methods

| Track | Current focus | Start here |
| --- | --- | --- |
| Lean 4 | Types, propositions, induction, structures, and verified programs | [Lean learning path](./Lean/README.md) |
| Coq / Rocq | Definitions, inductive types, tactics, and proofs | [Coq learning path](./Coq/README.md) |

### Ecosystems and applications

| Track | Current focus | Start here |
| --- | --- | --- |
| Spring Boot | A layered product-management REST example | [Spring Boot example](./Spring/ProductExample/README.md) |
| Python Data & ML | NumPy plus roadmaps for the wider data ecosystem | [Python learning path](./Python/README.md) |

See [PROGRESS.md](./PROGRESS.md) for the exact material currently available and
the gaps in each track. Planned content is explicitly distinguished from
executable lessons.

## How to study

1. Select one track and read its prerequisites and lesson order.
2. Predict what an example will do before executing it.
3. Reimplement the central idea without looking at the solution.
4. Complete or extend the exercises.
5. Run the relevant checks after every change.
6. Compare the concept with another language or paradigm.

The examples are reference material, but the repository is designed for active
practice rather than passive reading.

## Verify the repository

On Windows, run every check supported by the toolchains installed locally:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\verify.ps1
```

The script reports missing toolchains as skipped and returns a non-zero exit
code when an available check fails. The
[GitHub Actions workflow](./.github/workflows/verify.yml) verifies each
ecosystem independently on every push and pull request.

Before publishing or tagging a release, require every local toolchain instead
of accepting skipped checks:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\verify.ps1 -RequireAll
```

Strict verification exits with code `2` when any supported toolchain or
required dependency is unavailable.

Individual setup and execution commands are documented in each track. The main
toolchain targets are C17, Java 17, Scala 3, Python 3.12, Lean 4.19, and Coq 8.x.

## Repository principles

- **Clarity over breadth:** a focused lesson is preferable to an unexplained
  collection of features.
- **Executable knowledge:** examples should compile or run when practical.
- **Honest status:** roadmaps and incomplete work are labelled as such.
- **Progressive learning:** files and concepts follow an intentional order.
- **Meaningful verification:** tests and builds are part of the material.
- **Readable decisions:** comments explain why a choice was made, not merely
  what the syntax does.

The complete authoring rules are in the
[editorial guide](./docs/EDITORIAL_GUIDE.md).

## Contributing

Corrections, clearer explanations, exercises, tests, and focused new lessons
are welcome. Before opening a pull request, read
[CONTRIBUTING.md](./CONTRIBUTING.md) and the
[Code of Conduct](./CODE_OF_CONDUCT.md).

## Project status

This is a growing reference, not a claim of exhaustive coverage. Stable,
verified material and future directions are tracked in
[PROGRESS.md](./PROGRESS.md).

## License

Released under the [MIT License](./LICENSE).
