public class PrimitiveTypes {
    public static void main(String[] args) {
        // Integer types
        byte smallNumber = 127;            // Maximum value for a byte
        short shortNumber = 32000;         // Near the upper limit for a short
        int intNumber = 100000;
        long longNumber = 10000000000L;    // Suffix 'L' indicates a long literal
        
        // Floating-point types
        float floatNumber = 3.14f;         // Suffix 'f' indicates a float literal
        double doubleNumber = 3.14159265359;
        
        // Character type
        char letter = 'A';
        
        // Boolean type
        boolean isJavaFun = true;
        
        // Arithmetic operations on integers
        int sum = intNumber + 5000;
        int difference = intNumber - 5000;
        int product = intNumber * 2;
        int quotient = intNumber / 2;
        int remainder = intNumber % 3;
        
        // Demonstrate type casting and promotion:
        // When performing arithmetic on bytes, the result is promoted to int.
        byte anotherSmallNumber = 10;
        byte byteSum = (byte)(smallNumber + anotherSmallNumber); // explicit cast is required
        
        // Casting a double to an int truncates the decimal part
        int truncatedDouble = (int) doubleNumber;
        
        // Arithmetic with characters:
        // Adding an integer to a char advances its Unicode value.
        char nextLetter = (char)(letter + 1); // 'A' becomes 'B'
        
        // Boolean operations:
        // Logical AND and OR operations.
        boolean andResult = isJavaFun && false;
        boolean orResult = isJavaFun || false;
        
        // Compound assignment operators demonstration
        int compound = 10;
        compound += 5;   // Equivalent to compound = compound + 5; Now compound is 15
        compound *= 2;   // Equivalent to compound = compound * 2; Now compound is 30
        
        // Demonstrate overflow behavior:
        // Incrementing a byte at its maximum value causes an overflow.
        byte overflowByte = 127;
        overflowByte++;  // Overflow: 127 becomes -128
        
        // Output all values and results to the console
        System.out.println("Byte value: " + smallNumber);
        System.out.println("Short value: " + shortNumber);
        System.out.println("Int value: " + intNumber);
        System.out.println("Long value: " + longNumber);
        System.out.println("Float value: " + floatNumber);
        System.out.println("Double value: " + doubleNumber);
        System.out.println("Char value: " + letter);
        System.out.println("Boolean value: " + isJavaFun);
        
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: " + product);
        System.out.println("Quotient: " + quotient);
        System.out.println("Remainder: " + remainder);
        
        System.out.println("Byte sum (with casting): " + byteSum);
        System.out.println("Truncated double (from " + doubleNumber + "): " + truncatedDouble);
        System.out.println("Next letter after " + letter + ": " + nextLetter);
        
        System.out.println("Boolean AND (true && false): " + andResult);
        System.out.println("Boolean OR (true || false): " + orResult);
        
        System.out.println("Compound assignment result: " + compound);
        System.out.println("Overflow example (byte 127 + 1): " + overflowByte);
    }
}

/*
Additional Explanation:

1. Primitive Data Types:
   - byte: 8-bit signed integer (-128 to 127).
   - short: 16-bit signed integer (-32,768 to 32,767).
   - int: 32-bit signed integer.
   - long: 64-bit signed integer, with the 'L' suffix to denote a long literal.
   - float: 32-bit floating-point number, with the 'f' suffix.
   - double: 64-bit floating-point number.
   - char: Single 16-bit Unicode character.
   - boolean: Represents a truth value, either true or false.

2. Arithmetic Operations:
   - Basic arithmetic operators include addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).

3. Type Casting and Promotion:
   - When performing arithmetic on types smaller than int (such as byte and short), Java automatically promotes them to int.
   - Explicit casting is necessary when converting the result back to a smaller type.
   - Casting from a floating-point number to an integer truncates the decimal part.

4. Character Arithmetic:
   - Characters can be manipulated numerically because they are represented by Unicode values.

5. Compound Assignment:
   - Operators like += and *= combine an arithmetic operation with assignment.

6. Overflow Behavior:
   - Primitive types have fixed sizes. Incrementing a byte at its maximum value causes it to wrap around to its minimum value.
*/
