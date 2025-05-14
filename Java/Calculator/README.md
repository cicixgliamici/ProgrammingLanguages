# Java Calculator Project

A simple calculator implementation in Java that demonstrates:
- Basic mathematical operations
- Exception handling
- Unit testing with JUnit 5
- Best practices in Java development

## Features

The calculator supports the following operations:
- Addition
- Subtraction
- Multiplication
- Division
- Power calculation

## Error Handling

The calculator includes robust error handling for:
- Division by zero
- Overflow conditions
- Invalid mathematical operations
- General calculation errors

## Testing

The project includes comprehensive unit tests that demonstrate:
- Basic operation testing
- Edge case handling
- Exception testing
- Multiple operation testing

## Project Structure

```
Calculator/
├── Calculator.java           # Main calculator implementation
├── CalculatorException.java  # Custom exception class
├── CalculatorTest.java      # JUnit test suite
└── README.md                # This file
```

## Running the Tests

To run the tests, you need:
1. Java Development Kit (JDK) 8 or higher
2. JUnit 5

You can run the tests using:
- Your favorite IDE (Eclipse, IntelliJ IDEA, etc.)
- Maven: `mvn test`
- Gradle: `gradle test`

## Best Practices Demonstrated

1. **Exception Handling**
   - Custom exception class
   - Specific error messages
   - Proper exception chaining

2. **Testing**
   - Comprehensive test coverage
   - Clear test names and descriptions
   - Testing of edge cases
   - Exception testing

3. **Code Quality**
   - Clear documentation
   - Consistent code style
   - Input validation
   - Result validation

## Future Improvements

Potential areas for enhancement:
- Add more mathematical operations
- Implement a command-line interface
- Add a graphical user interface
- Support for complex numbers
- Add performance benchmarks 