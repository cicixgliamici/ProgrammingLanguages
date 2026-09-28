# Global Learning Progress

This document is the repository-wide index of implemented material. It records
what can be studied or executed today and separates it from topics that are only
planned. Update the relevant row whenever a lesson, exercise, test, or project
is added.

## Status legend

- **Implemented**: source code or a complete lesson is present.
- **In progress**: useful material exists, but the section is not yet a complete learning path.
- **Planned**: the directory contains only an introduction or roadmap.

## Progress overview

| Area | Status | Implemented structures and features | Main gaps |
| --- | --- | --- | --- |
| [C](./C/) | In progress | Basic program structure; bitwise operations; manual memory management; linked list; queue; stack; binary search; binary search tree; introductory Exercism solutions; CMake build and CTest smoke tests | Section README, focused unit tests, ownership/error-handling conventions |
| [Java](./Java/) | In progress | Syntax and primitive types; strings; arrays; math utilities; array algorithms; exceptions; generic doubly linked list; calculator; JUnit examples; Maven build | Package structure, collection interfaces, broader test automation |
| [Scala](./Scala/) | In progress | Basic syntax; values and functions; functional programming; strings; collections; classes and traits; sbt build | Section README, tests, pattern matching, algebraic data types, concurrency |
| [Python](./Python/) | In progress | Core syntax and collections; iterators and generators; OOP, protocols, and dataclasses; exceptions, files, and JSON; arrays and hashing; token-bucket rate limiter; linear regression; password hashing and login protection; NumPy foundations through linear algebra and data preparation; standard-library unit tests | Packaging; executable lessons for pandas, Matplotlib, scikit-learn, TensorFlow, and PyTorch |
| [Lean 4](./Lean/) | Implemented | Typed functions; propositions and tactics; rewriting; pattern matching; structures; recursion and induction; lists and trees; `Option`; products and sums; typeclasses; dependent vectors; verified expression optimization; pinned toolchain and CI verification | Lake module structure, larger multi-module examples |
| [Coq / Rocq](./Coq/) | In progress | Definitions and computation; propositions; equality rewriting; inductive types; lists; structural induction; deterministic project file and CI verification | More advanced proofs and extraction |
| [Spring Boot](./Spring/ProductExample/) | In progress | Layered CRUD example with application, controller, service, repository, and JPA entity; Maven configuration; service unit tests | README/API examples, validation, exception mapping, database configuration and migrations |

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
| `HelloWorld.java`, `PrimitiveTypes.java` | Program structure and primitive values |
| `StringOperations.java`, `MathFunctions.java` | Standard string and numerical operations |
| `ArrayOperations.java`, `ArrayAlgorithms.java` | Array manipulation and algorithms |
| `Calculator/` | Arithmetic operations, custom exceptions, and JUnit tests |
| `DoublyLinkedList/` | Generic nodes, bidirectional links, list operations, and JUnit tests |

### Scala

The numbered examples currently progress from basic syntax to functional
programming, string processing, collections, and object-oriented modelling with
classes and traits.

### Python

| Section | Status | Coverage |
| --- | --- | --- |
| [`standard_library`](./Python/standard_library/) | Implemented | Nine progressive topics, including system-design, ML, and security sketches |
| [`numpy`](./Python/numpy/) | Implemented | Arrays, dtypes, indexing, views/copies, broadcasting, reductions, random data, linear algebra, reshaping, missing data, sorting, and searching |
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

The example uses Maven and Spring Data JPA. It is currently an implementation
sample rather than a documented, tested application.

## Updating this index

When adding material:

1. Add the new file to the relevant detailed section or linked section README.
2. Describe only features that are present in source code.
3. Move a section from **Planned** only when it contains an executable example.
4. Record tests and reproducible build commands as part of progress, not as optional polish.
5. Keep future ideas in the **Main gaps** column so planned work is not confused with completed work.
