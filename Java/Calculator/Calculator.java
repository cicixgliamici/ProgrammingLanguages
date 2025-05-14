/**
 * A simple calculator class that performs basic mathematical operations.
 * This class is used to demonstrate unit testing in Java.
 */
public class Calculator {
    
    /**
     * Adds two numbers
     * @param a first number
     * @param b second number
     * @return sum of a and b
     * @throws CalculatorException if the result is invalid
     */
    public double add(double a, double b) {
        try {
            double result = a + b;
            if (Double.isInfinite(result)) {
                throw new CalculatorException("Result is too large to be represented");
            }
            return result;
        } catch (Exception e) {
            throw new CalculatorException("Error during addition", e);
        }
    }
    
    /**
     * Subtracts second number from first number
     * @param a first number
     * @param b second number
     * @return difference between a and b
     * @throws CalculatorException if the result is invalid
     */
    public double subtract(double a, double b) {
        try {
            double result = a - b;
            if (Double.isInfinite(result)) {
                throw new CalculatorException("Result is too large to be represented");
            }
            return result;
        } catch (Exception e) {
            throw new CalculatorException("Error during subtraction", e);
        }
    }
    
    /**
     * Multiplies two numbers
     * @param a first number
     * @param b second number
     * @return product of a and b
     * @throws CalculatorException if the result is invalid
     */
    public double multiply(double a, double b) {
        try {
            double result = a * b;
            if (Double.isInfinite(result)) {
                throw new CalculatorException("Result is too large to be represented");
            }
            return result;
        } catch (Exception e) {
            throw new CalculatorException("Error during multiplication", e);
        }
    }
    
    /**
     * Divides first number by second number
     * @param a first number (dividend)
     * @param b second number (divisor)
     * @return quotient of a divided by b
     * @throws CalculatorException if b is zero or result is invalid
     */
    public double divide(double a, double b) {
        if (b == 0) {
            throw new CalculatorException("Division by zero is not allowed");
        }
        try {
            double result = a / b;
            if (Double.isInfinite(result)) {
                throw new CalculatorException("Result is too large to be represented");
            }
            return result;
        } catch (Exception e) {
            throw new CalculatorException("Error during division", e);
        }
    }
    
    /**
     * Calculates the power of a number
     * @param base the base number
     * @param exponent the exponent
     * @return base raised to the power of exponent
     * @throws CalculatorException if the result is invalid
     */
    public double power(double base, double exponent) {
        try {
            double result = Math.pow(base, exponent);
            if (Double.isInfinite(result)) {
                throw new CalculatorException("Result is too large to be represented");
            }
            if (Double.isNaN(result)) {
                throw new CalculatorException("Invalid power operation");
            }
            return result;
        } catch (Exception e) {
            throw new CalculatorException("Error during power calculation", e);
        }
    }
} 