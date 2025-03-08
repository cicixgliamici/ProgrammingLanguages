public class Math {
    public static void main(String[] args) {
        double a = 9.0;
        double b = 2.0;

        System.out.println("Square root of " + a + ": " + Math.sqrt(a));
        System.out.println("Power (" + a + "^" + b + "): " + Math.pow(a, b));
        System.out.println("Absolute value of -" + a + ": " + Math.abs(-a));
        System.out.println("Ceiling of " + a + ": " + Math.ceil(a));
        System.out.println("Floor of " + a + ": " + Math.floor(a));
        System.out.println("Max between " + a + " and " + b + ": " + Math.max(a, b));
        System.out.println("Min between " + a + " and " + b + ": " + Math.min(a, b));
        System.out.println("Random number (0 to 1): " + Math.random());
    }
}

/*
Explanation:

1. `public class MathFunctions { ... }`
   - Defines a public class named `MathFunctions`.
   - The program is contained within this class.

2. `public static void main(String[] args) { ... }`
   - This is the main method, the program's entry point.
   - The structure is the same as explained before.

3. `double a = 9.0; double b = 2.0;`
   - Declares two double precision floating-point numbers.

4. `Math.sqrt(a)`
   - Computes the square root of `a`.

5. `Math.pow(a, b)`
   - Computes `a` raised to the power of `b`.

6. `Math.abs(-a)`
   - Returns the absolute value of `-a`.

7. `Math.ceil(a)` and `Math.floor(a)`
   - `ceil()`: Rounds `a` up to the nearest integer.
   - `floor()`: Rounds `a` down to the nearest integer.

8. `Math.max(a, b)` and `Math.min(a, b)`
   - `max()`: Returns the larger of `a` and `b`.
   - `min()`: Returns the smaller of `a` and `b`.

9. `Math.random()`
   - Generates a random number between 0.0 and 1.0.
*/
