# Global Learning Progress

This document is the repository-wide index of implemented material. It records
what can be studied or executed today and separates it from topics that are only
planned. Update the relevant row whenever a lesson, exercise, test, or project
is added.

## Status legend

- **Planned**: a roadmap exists, but no executable lesson is available.
- **Draft**: useful material exists, but the learning path is incomplete.
- **Usable**: the section has instructions, executable material, and exercises.
- **Verified**: the material is automatically built or tested in CI.
- **Complete**: the defined learning objectives and final project are present.

## Progress overview

| Area | Status | Implemented structures and features | Main gaps |
| --- | --- | --- | --- |
| [C](./C/) | Verified | Basic program structure; bitwise operations; manual memory management; linked list; queue; stack; binary search; binary search tree; introductory Exercism solutions; CMake build; smoke and focused CTest tests | More data-structure unit tests, ownership/error-handling conventions |
| [Java](./Java/) | Verified | Syntax and primitive types; strings; arrays; math utilities; array algorithms; exceptions; generic doubly linked list; calculator; conventional Maven packages; JUnit examples | Collection interfaces and broader test automation |
| [Scala](./Scala/) | Verified | Basic syntax; values and functions; functional programming; strings; collections; classes and traits; conventional sbt layout; MUnit tests | Pattern matching, algebraic data types, concurrency, broader tests |
| [Python](./Python/) | Verified | Core syntax and collections; iterators and generators; OOP, protocols, and dataclasses; exceptions, files, and JSON; arrays and hashing; token-bucket rate limiter; linear regression; password hashing and login protection; pinned NumPy track; standard-library tests and CI lesson execution | Packaging; focused NumPy unit tests; executable lessons for pandas, Matplotlib, scikit-learn, TensorFlow, and PyTorch |
| [Lean 4](./Lean/) | Verified | Typed functions; propositions and tactics; rewriting; pattern matching; structures; recursion and induction; lists and trees; `Option`; products and sums; typeclasses; dependent vectors; verified expression optimization; pinned Lake build and CI verification | Larger multi-module examples and final project criteria |
| [Coq / Rocq](./Coq/) | Verified | Definitions and computation; propositions; equality rewriting; inductive types; lists; structural induction; namespaced `_CoqProject` and generated Makefile build | More advanced proofs, exercises, and extraction |
| [Spring Boot](./Spring/ProductExample/) | Verified | Layered CRUD example with application, controller, service, repository, and JPA entity; Maven configuration; service unit tests; API and architecture guide | Validation, exception mapping, controller tests, database configuration and migrations |

## Detailed index

### C

| File | Topic |
| --- | --- |
| `00_helloWorld.c` | Compilation unit and console output |
| `01_bitwise_operations.c` | Bit masks, shifts, flags, and binary operations |
| `02_list.c` | Linked-list operations |
| `03_memory_management_intro.c` | Pointers, allocation, cleanup, and ownership basics |
| `04_queue.c` | Queue data structure |
| `05_stack.c` | Stack data structure |
| `06_binary_search.c` | Binary search |
| `07_binary_search_tree.c` | Binary-search-tree operations |
| `Exercism/` | Small standalone exercises |

### Java

| Material | Topic |
| --- | --- |
| `00_Introduction.md` | Language overview and foundational notes |
| `src/main/java/dev/learning/basics/` | Program structure, primitive values, strings, math, arrays, and algorithms |
| `src/main/java/dev/learning/calculator/` | Arithmetic operations and custom exceptions |
| `src/main/java/dev/learning/collections/` | Generic nodes and bidirectional list operations |
| `src/test/java/` | JUnit tests for reusable behavior and invariants |

### Scala

The numbered examples in `src/main/scala` progress from basic syntax to
functional programming, string processing, collections, and object-oriented
modelling with classes and traits. MUnit tests live in `src/test/scala`.

### Python

| Section | Status | Coverage |
| --- | --- | --- |
| [`standard_library`](./Python/standard_library/) | Verified | Nine progressive topics, including system-design, ML, and security sketches |
| [`numpy`](./Python/numpy/) | Verified | Arrays, dtypes, indexing, views/copies, broadcasting, reductions, random data, linear algebra, reshaping, missing data, sorting, and searching |
| [`pandas`](./Python/pandas/) | Planned | README roadmap only |
| [`matplotlib`](./Python/matplotlib/) | Planned | README roadmap only |
| [`scikit_learn`](./Python/scikit_learn/) | Planned | README roadmap only |
| [`tensorflow`](./Python/tensorflow/) | Planned | README roadmap only |
| [`pytorch`](./Python/pytorch/) | Planned | README roadmap only |

### Lean 4

The [Lean learning path](./Lean/README.md) is the most complete section. Its 20
numbered files move from definitions and propositional logic to induction,
custom inductive types, list and tree proofs, generic programming, dependent
types, and a verified optimizer.

### Coq / Rocq

The [Coq learning path](./Coq/README.md) contains six numbered lessons. It
currently covers the foundations through recursive list and natural-number
proofs.

### Spring Boot

`ProductExample` demonstrates the conventional dependency flow:

`HTTP controller -> service interface -> service implementation -> repository -> entity`

The example uses Maven and Spring Data JPA. Its architecture, API, limitations,
tests, and extension exercises are documented in the section README.

## Updating this index

When adding material:

1. Add the new file to the relevant detailed section or linked section README.
2. Describe only features that are present in source code.
3. Move a section from **Planned** only when it contains an executable example.
4. Record tests and reproducible build commands as part of progress, not as optional polish.
5. Keep future ideas in the **Main gaps** column so planned work is not confused with completed work.
