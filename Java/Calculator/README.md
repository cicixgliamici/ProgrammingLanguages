# Java Calculator

This example demonstrates arithmetic operations, a domain-specific unchecked
exception, and unit testing with JUnit 5.

## Features

- Addition, subtraction, multiplication, division, and exponentiation.
- Explicit failures for division by zero and non-finite results.
- Tests for normal operations, boundary conditions, and exceptions.

## Project structure

```text
src/main/java/dev/learning/calculator/
|-- Calculator.java
`-- CalculatorException.java

src/test/java/dev/learning/calculator/
`-- CalculatorTest.java
```

The source and test directories follow Maven conventions. The package boundary
keeps the example independent from the introductory language lessons.

## Run the tests

From the repository root:

```powershell
mvn --file Java/pom.xml test
```

## Study exercises

1. Add parameterized tests for a table of arithmetic cases.
2. Decide how `NaN` inputs should behave and encode the decision in tests.
3. Add one operation without catching exceptions that the operation cannot
   meaningfully handle.
4. Compare the current unchecked exception with a checked-exception API.
