package dev.learning.basics;

public class MathFunctions {
    public static void main(String[] args) {
        // 1. Declaration and initialization of two double values
        double a = 9.0;
        double b = 2.0;
        double angleDegrees = 45.0; // Angle in degrees for trigonometric functions

        // Basic Math operations:

        // 2. Square root: Computes the square root of 'a'
        System.out.println("Square root of " + a + ": " + Math.sqrt(a));

        // 3. Power: Computes 'a' raised to the power of 'b'
        System.out.println("Power (" + a + "^" + b + "): " + Math.pow(a, b));

        // 4. Absolute value: Returns the absolute value of -a
        System.out.println("Absolute value of -" + a + ": " + Math.abs(-a));

        // 5. Ceiling: Rounds 'a' up to the nearest integer
        System.out.println("Ceiling of " + a + ": " + Math.ceil(a));

        // 6. Floor: Rounds 'a' down to the nearest integer
        System.out.println("Floor of " + a + ": " + Math.floor(a));

        // 7. Maximum: Returns the larger value between 'a' and 'b'
        System.out.println("Max between " + a + " and " + b + ": " + Math.max(a, b));

        // 8. Minimum: Returns the smaller value between 'a' and 'b'
        System.out.println("Min between " + a + " and " + b + ": " + Math.min(a, b));

        // 9. Random: Generates a random number between 0.0 (inclusive) and 1.0 (exclusive)
        System.out.println("Random number (0 to 1): " + Math.random());

        // Additional Math operations:

        // 10. Trigonometric Functions:
        // Convert angle from degrees to radians
        double angleRadians = Math.toRadians(angleDegrees);
        System.out.println("Sine of " + angleDegrees + " degrees: " + Math.sin(angleRadians));
        System.out.println("Cosine of " + angleDegrees + " degrees: " + Math.cos(angleRadians));
        System.out.println("Tangent of " + angleDegrees + " degrees: " + Math.tan(angleRadians));

        // 11. Logarithmic and Exponential Functions:
        // Natural logarithm (base e) of 'a'
        System.out.println("Natural logarithm (ln) of " + a + ": " + Math.log(a));
        // Logarithm base 10 of 'a'
        System.out.println("Log base 10 of " + a + ": " + Math.log10(a));
        // Exponential: e raised to the power of 'b'
        System.out.println("Exponential of " + b + " (e^" + b + "): " + Math.exp(b));

        // 12. Rounding Functions:
        // Math.round: Rounds 'a' to the nearest integer and returns a long
        System.out.println("Rounded value of " + a + ": " + Math.round(a));
        // Math.rint: Returns the double value that is closest to 'a' and equal to a mathematical integer
        System.out.println("Rint (closest integer) of " + a + ": " + Math.rint(a));

        // 13. Angle Conversion:
        // Convert radians back to degrees
        double radians = Math.PI / 4; // 45 degrees in radians
        System.out.println("Radians " + radians + " in degrees: " + Math.toDegrees(radians));
    }
}

/*
Explanation:

1. public class MathFunctions { ... }
   - Defines a public class named MathFunctions that contains the program.

2. public static void main(String[] args) { ... }
   - The main method is the entry point of the program.

3. double a = 9.0; double b = 2.0; double angleDegrees = 45.0;
   - Declares and initializes double precision variables for performing math operations.
   
4. Math.sqrt(a)
   - Computes the square root of 'a'.

5. Math.pow(a, b)
   - Computes 'a' raised to the power of 'b'.

6. Math.abs(-a)
   - Returns the absolute value of '-a'.

7. Math.ceil(a) and Math.floor(a)
   - Rounds 'a' up (ceiling) and down (floor) respectively.

8. Math.max(a, b) and Math.min(a, b)
   - Returns the maximum and minimum values between 'a' and 'b'.

9. Math.random()
   - Generates a random number between 0.0 and 1.0.

10. Trigonometric Functions:
    - Math.toRadians(angleDegrees) converts an angle from degrees to radians.
    - Math.sin, Math.cos, and Math.tan calculate the sine, cosine, and tangent of an angle (in radians).

11. Logarithmic and Exponential Functions:
    - Math.log(a) computes the natural logarithm (base e) of 'a'.
    - Math.log10(a) computes the logarithm base 10 of 'a'.
    - Math.exp(b) computes the exponential function of 'b' (e^b).

12. Rounding Functions:
    - Math.round(a) rounds 'a' to the nearest integer.
    - Math.rint(a) returns the closest double value that is mathematically an integer.

13. Angle Conversion:
    - Math.toDegrees(radians) converts an angle from radians back to degrees.
*/
