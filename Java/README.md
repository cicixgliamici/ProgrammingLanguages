# Learning Java

This track introduces Java 17 through executable examples, two small data
structures, and JUnit tests. It focuses on syntax, object-oriented design,
arrays, exceptions, generics, and the distinction between an implementation and
its observable contract.

## Prerequisites

- Basic programming concepts such as variables, conditions, loops, and
  functions.
- JDK 17 and Maven 3.9 or a compatible version.

Start with [`00_Introduction.md`](./00_Introduction.md) when a theoretical
overview is useful, then use the executable files for practice.

## Learning path

| Material | Learning objective |
| --- | --- |
| `src/main/java/dev/learning/basics/` | Study entry points, primitive types, strings, math, arrays, and algorithms. |
| `src/main/java/dev/learning/calculator/` | Model failures with a custom exception. |
| `src/main/java/dev/learning/collections/` | Implement a generic linked structure. |
| `src/test/java/` | Verify calculator behavior and list invariants with JUnit. |

## Compile and test

From the repository root:

```powershell
mvn --file Java/pom.xml verify
```

Maven compiles all examples and runs the JUnit test classes. Run a compiled
entry point from the `Java` directory, for example:

```powershell
Set-Location Java
mvn compile
java -cp target/classes dev.learning.basics.HelloWorld
```

## Study method

Read the public API of an example before its implementation. Write down its
preconditions, result, and possible failures. For the calculator and linked
list, add one test before changing behavior so the intended contract remains
visible.

Suggested exercises:

1. Add boundary tests for every array algorithm.
2. Implement iteration for the doubly linked list.
3. Compare checked and unchecked exception designs for the calculator.
4. Replace one index-based loop with an enhanced loop or stream and explain
   whether readability improves.

## Common mistakes

- Comparing strings with `==` instead of `equals`.
- Exposing mutable internal collections or nodes.
- Confusing primitive values with reference types.
- Catching exceptions without handling or communicating the failure.
- Testing implementation details instead of public behavior.

## Project layout

The project uses Maven's conventional `src/main/java` and `src/test/java`
directories. Packages group foundational lessons, the calculator, and the
collection example without mixing production code and tests.

## Further reading

- [Java language documentation](https://docs.oracle.com/en/java/javase/17/)
- [JUnit 5 user guide](https://junit.org/junit5/docs/current/user-guide/)
- [Maven getting started guide](https://maven.apache.org/guides/getting-started/)
