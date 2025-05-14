/**
 * Custom exception class for calculator operations
 * This class provides more specific error handling for calculator operations
 */
public class CalculatorException extends RuntimeException {
    
    /**
     * Creates a new CalculatorException with a message
     * @param message the error message
     */
    public CalculatorException(String message) {
        super(message);
    }
    
    /**
     * Creates a new CalculatorException with a message and cause
     * @param message the error message
     * @param cause the original exception that caused this exception
     */
    public CalculatorException(String message, Throwable cause) {
        super(message, cause);
    }
} 