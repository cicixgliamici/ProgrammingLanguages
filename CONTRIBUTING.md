# Contributing

Thank you for helping make this repository a clearer and more reliable learning
resource. Contributions are welcome when they improve an existing explanation,
add meaningful verification, or extend a learning path in a focused way.

## Before starting

1. Read the relevant track README and its implemented lesson index.
2. Check existing issues and pull requests to avoid duplicate work.
3. Open an issue before proposing a new language, framework, or large
   structural change.
4. Follow the style rules below and the [Code of Conduct](./CODE_OF_CONDUCT.md).

Small corrections and focused test improvements do not require an issue first.

## What makes a useful contribution

A new lesson should normally include:

- one explicit learning objective;
- prerequisites and its place in the learning sequence;
- a small, readable, executable example;
- comments that explain non-obvious decisions;
- at least one exercise, test, or observable result;
- documentation of any new dependency or command;
- an update to the relevant public track index.

Avoid adding isolated snippets, generated output, copied tutorials, or broad
files that cover many unrelated concepts.

## Development workflow

1. Fork the repository and create a focused branch.
2. Make the smallest coherent change that solves the problem.
3. Run the checks for the affected language.
4. Run the repository verification script when the required tools are present:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\scripts\verify.ps1
   ```

5. Update documentation when behavior, prerequisites, or commands change.
6. Open a pull request using the provided template.

If a local toolchain is unavailable, state exactly which check was not run. The
continuous-integration workflow will still validate the supported ecosystems.

## Code and documentation style

- Write code, comments, documentation, commit messages, and pull-request text
  in English.
- Prefer short functions with descriptive names.
- Explain why a decision matters; do not narrate obvious syntax.
- Keep examples self-contained unless the lesson explicitly teaches modules.
- Use platform-neutral commands where practical and document alternatives when
  commands differ between Windows and Unix-like systems.
- Preserve the established teaching order and naming convention in each track.
- Do not commit build output, editor settings, environments, credentials, or
  personal absolute paths.

## Pull requests

Keep each pull request focused on one lesson, correction, or infrastructure
improvement. A reviewer should be able to understand the learning goal, inspect
the change, and reproduce its verification without unrelated context.

By contributing, you agree that your contribution is licensed under the
[MIT License](./LICENSE).
