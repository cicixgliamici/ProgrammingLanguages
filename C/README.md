# Learning C

This track introduces C17 through small executable programs. It begins with the
compilation model and bitwise operations, then moves to pointers, manual memory
management, data structures, and search algorithms.

## Prerequisites

- Basic familiarity with variables, conditions, loops, and functions.
- A C17 compiler and CMake 3.20 or newer.

No previous experience with pointers or manual memory management is required.

## Lesson index

| File | Learning objective |
| --- | --- |
| `00_helloWorld.c` | Understand the smallest executable C program. |
| `01_bitwise_operations.c` | Use masks, shifts, and flags deliberately. |
| `02_list.c` | Build and traverse a singly linked list. |
| `03_memory_management_intro.c` | Allocate, own, and release dynamic memory. |
| `04_queue.c` | Implement first-in, first-out behavior. |
| `05_stack.c` | Implement last-in, first-out behavior. |
| `06_binary_search.c` | Search sorted data while maintaining interval invariants. |
| `07_binary_search_tree.c` | Insert, find, traverse, and release tree nodes. |
| `Exercism/` | Practice with small standalone exercises. |

The data-structure files are teaching examples rather than reusable production
libraries. Their implementations and demonstrations intentionally live
together so that ownership and control flow remain visible.

Focused tests in `tests/` verify binary-search boundary cases and Gregorian
leap-year rules. CTest also runs every complete lesson as a smoke test.

## Build and run

From the repository root:

```powershell
cmake -S C -B build/c
cmake --build build/c
ctest --test-dir build/c --output-on-failure
```

Executables are written below `build/c`; their exact paths depend on the
selected CMake generator and build configuration.

On macOS or Linux, the same CMake commands work in a shell. A compiler can also
build one independent lesson directly, for example:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic C/06_binary_search.c -o binary_search
./binary_search
```

## Study method

For each lesson, identify the lifetime of every value, write down the data
structure invariant, and predict the output before running the program. For
dynamic structures, trace which function owns each allocation and where it is
released.

Useful extensions include adding an invalid-input case, checking every
allocation failure, and writing an assertion for each public operation.

## Common mistakes

- Dereferencing a null or uninitialized pointer.
- Losing the only pointer to allocated memory.
- Reading memory after it has been freed.
- Forgetting that array indices range from zero to `length - 1`.
- Applying binary search to unsorted input.
- Updating only one link or boundary when a data structure changes.

## Further reading

- [C language reference](https://en.cppreference.com/w/c/language)
- [CMake tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/)
