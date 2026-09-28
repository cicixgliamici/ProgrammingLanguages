# Programming Languages Reference & Practice

This repository collects notes, examples, and small implementations related to programming languages and core programming concepts.

Its goal is to be a **growing reference and practice space** rather than a finished encyclopedic resource.

The repository is especially useful for:
- revising language fundamentals,
- comparing idioms across languages,
- studying small implementations of core concepts,
- and building structured material for practice and interview preparation.

The current implementation status and covered features are tracked in the
[global learning progress index](./PROGRESS.md).

---

## Why this repository matters

A lot of language-learning repositories try to cover everything at once.

This one is intentionally more modest and more honest in scope: it is a repository that grows over time through curated examples, notes, and small exercises.

The value of the project lies in:
- **clarity over breadth**,
- **practice-oriented structure**,
- and the possibility of comparing different languages through concrete material.

---

## Repository structure

The repository is organized by language, with each language area potentially containing:
- syntax and basic concepts
- data structures
- algorithmic patterns
- small exercises or mini-projects
- notes on style, best practices, and recurring ideas

### Current visible language areas
- [C Programming](./C/)
- [Java](./Java/)
- [Scala](./Scala/)
- [Python](./Python/)
- [Lean4](./Lean/)
- [Coq / Rocq](./Coq/)
- [SpringBoot](./Spring/)

As the repository evolves, more language sections can be added in the same spirit.

---

## How to use this repository

A practical way to use it is:

1. Read the notes or examples for a language area.
2. Re-implement the idea independently.
3. Compare approaches across different languages.
4. Use the repository as a revision and practice base rather than as a passive reference only.

## Verify the repository

Run all checks supported by the tools installed on the current machine:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\verify.ps1
```

The script compiles or checks C, Java, Spring Boot, Scala, Python, Lean, and
Coq. Missing toolchains are reported as skipped, while a failed available check
returns a non-zero exit code. Language-specific build files pin the relevant
language or build-tool versions where practical.

The workflow in `.github/workflows/verify.yml` runs the same responsibilities
in isolated CI jobs. Keeping one job per ecosystem makes failures easy to
locate and prevents an unavailable toolchain from hiding results for the other
languages.

---

## Positioning

This repository is best understood as:
- a **study and practice repository**,
- a **curated personal reference**,
- and a place to organize programming-language material in a structured way.

It is not meant to claim exhaustive coverage of every language or topic.

---

## Future directions

Possible future extensions include:
- more language sections
- additional algorithmic patterns
- notes on paradigms and language design
- comparisons between imperative, object-oriented, and functional approaches
- more mini-projects and guided exercises

These are directions for growth, not claims about what is already fully implemented.

---

## Contributing

Contributions, improvements, and corrections are welcome.

---

## License

MIT
