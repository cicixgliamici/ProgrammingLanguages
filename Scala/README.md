# Learning Scala 3

This track introduces Scala 3 as a language that combines functional and
object-oriented programming. The numbered examples progress from basic syntax
to first-class functions, collections, classes, case classes, and traits.

## Prerequisites

- Familiarity with basic programming concepts.
- JDK 17 or newer.
- sbt 1.11 or a compatible version.

Experience with Java is helpful but not required.

## Lesson index

| File | Learning objective |
| --- | --- |
| `00_HelloWorld.scala` | Recognize Scala 3 syntax and an `@main` entry point. |
| `01_FunctionalBasics.scala` | Treat functions as values and transform data. |
| `02_FunctionalBasics2.scala` | Compose functional techniques in a larger example. |
| `03_StringExamples.scala` | Transform and inspect immutable strings. |
| `04_Collections.scala` | Use immutable collections and higher-order operations. |
| `05_ClassesAndTraits.scala` | Model data and behavior with classes, case classes, and traits. |

## Compile and run

From the repository root:

```powershell
Set-Location Scala
sbt --batch test
```

To select and run one of the available `@main` entry points:

```powershell
sbt run
```

The build uses the conventional `src/main/scala` and `src/test/scala` layout.
Lessons remain numbered inside the `dev.learning.scalaexamples` package, while
MUnit tests verify reusable computations independently of console output.

## Study method

For every example, identify which values are immutable, which functions are
pure, and which expressions cause observable effects. Rewrite one collection
transformation with an explicit loop, then compare its state changes and
readability with the functional version.

Suggested exercises:

1. Express the same transformation with `map`, a comprehension, and recursion.
2. Add an algebraic data type with `enum` and exhaustive pattern matching.
3. Add tests for collection transformations.
4. Make an invalid state unrepresentable with a more precise type.

## Common mistakes

- Reading an expression-oriented construct as though it were only a statement.
- Introducing mutable state when a collection transformation is clearer.
- Using inheritance where a small algebraic data type is sufficient.
- Ignoring the difference between `Option` and a nullable value.
- Assuming a collection operation mutates its input.

## Further reading

- [Scala 3 book](https://docs.scala-lang.org/scala3/book/introduction.html)
- [Scala 3 reference](https://docs.scala-lang.org/scala3/reference/)
- [sbt documentation](https://www.scala-sbt.org/documentation.html)
