public class PrimitiveTypes {
    public static void main(String[] args) {
        // Integer types
        byte smallNumber = 127;
        short shortNumber = 32000;
        int intNumber = 100000;
        long longNumber = 10000000000L;
        
        // Floating-point types
        float floatNumber = 3.14f;
        double doubleNumber = 3.14159265359;
        
        // Character type
        char letter = 'A';
        
        // Boolean type
        boolean isJavaFun = true;
        
        // Arithmetic operations
        int sum = intNumber + 5000;
        int difference = intNumber - 5000;
        int product = intNumber * 2;
        int quotient = intNumber / 2;
        int remainder = intNumber % 3;
        
        // Output
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
    }
}

/*
Explanation:

1. `public class PrimitiveTypes { ... }`
   - Defines a public class named `PrimitiveTypes`.

2. `public static void main(String[] args) { ... }`
   - The main method, where the program execution starts.

3. Primitive data types:
   - `byte`: 8-bit integer (-128 to 127).
   - `short`: 16-bit integer (-32,768 to 32,767).
   - `int`: 32-bit integer (-2^31 to 2^31-1).
   - `long`: 64-bit integer (-2^63 to 2^63-1), needs `L` suffix.
   - `float`: 32-bit floating-point, needs `f` suffix.
   - `double`: 64-bit floating-point.
   - `char`: Single character enclosed in single quotes.
   - `boolean`: Stores `true` or `false`.

4. Arithmetic operations:
   - `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulus).

5. `System.out.println(...)`
   - Prints variable values to the console.
*/
