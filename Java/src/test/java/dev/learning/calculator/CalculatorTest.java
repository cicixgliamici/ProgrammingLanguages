package dev.learning.calculator;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for the Calculator
 * This class demonstrates various testing techniques in JUnit:
 * - Basic assertions
 * - Exception testing
 * - Multiple test cases
 * - Descriptive test names
 */
public class CalculatorTest {
    
    private final Calculator calculator = new Calculator();
    
    @Test
    @DisplayName("Test addition of two positive numbers")
    public void testAddPositiveNumbers() {
        assertEquals(5.0, calculator.add(2.0, 3.0), "2 + 3 should equal 5");
    }
    
    @Test
    @DisplayName("Test addition with negative numbers")
    public void testAddNegativeNumbers() {
        assertEquals(-1.0, calculator.add(2.0, -3.0), "2 + (-3) should equal -1");
    }
    
    @Test
    @DisplayName("Test addition with overflow")
    public void testAddOverflow() {
        Exception exception = assertThrows(CalculatorException.class, () -> {
            calculator.add(Double.MAX_VALUE, Double.MAX_VALUE);
        });
        assertEquals("Result is too large to be represented", exception.getMessage());
    }
    
    @Test
    @DisplayName("Test subtraction of two numbers")
    public void testSubtract() {
        assertEquals(1.0, calculator.subtract(3.0, 2.0), "3 - 2 should equal 1");
        assertEquals(-1.0, calculator.subtract(2.0, 3.0), "2 - 3 should equal -1");
    }
    
    @Test
    @DisplayName("Test multiplication of two numbers")
    public void testMultiply() {
        assertEquals(6.0, calculator.multiply(2.0, 3.0), "2 * 3 should equal 6");
        assertEquals(-6.0, calculator.multiply(2.0, -3.0), "2 * (-3) should equal -6");
    }
    
    @Test
    @DisplayName("Test multiplication with overflow")
    public void testMultiplyOverflow() {
        Exception exception = assertThrows(CalculatorException.class, () -> {
            calculator.multiply(Double.MAX_VALUE, 2.0);
        });
        assertEquals("Result is too large to be represented", exception.getMessage());
    }
    
    @Test
    @DisplayName("Test division of two numbers")
    public void testDivide() {
        assertEquals(2.0, calculator.divide(6.0, 3.0), "6 / 3 should equal 2");
        assertEquals(-2.0, calculator.divide(6.0, -3.0), "6 / (-3) should equal -2");
    }
    
    @Test
    @DisplayName("Test division by zero")
    public void testDivideByZero() {
        Exception exception = assertThrows(CalculatorException.class, () -> {
            calculator.divide(5.0, 0.0);
        });
        assertEquals("Division by zero is not allowed", exception.getMessage());
    }
    
    @Test
    @DisplayName("Test power calculation")
    public void testPower() {
        assertEquals(8.0, calculator.power(2.0, 3.0), "2^3 should equal 8");
        assertEquals(0.125, calculator.power(2.0, -3.0), "2^(-3) should equal 0.125");
    }
    
    @Test
    @DisplayName("Test invalid power operation")
    public void testInvalidPower() {
        Exception exception = assertThrows(CalculatorException.class, () -> {
            calculator.power(-2.0, 0.5); // Square root of negative number
        });
        assertEquals("Invalid power operation", exception.getMessage());
    }
    
    @Test
    @DisplayName("Test multiple operations in sequence")
    public void testMultipleOperations() {
        double result = calculator.add(
            calculator.multiply(2.0, 3.0),
            calculator.divide(6.0, 2.0)
        );
        assertEquals(9.0, result, "(2 * 3) + (6 / 2) should equal 9");
    }
} 
