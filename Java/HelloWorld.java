public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

/*
Explanation:

1. `public class HelloWorld { ... }`
   - Defines a public class named `HelloWorld`.
   - In Java, every program must be contained within a class.
   - The class name must match the filename (`HelloWorld.java`).

2. `public static void main(String[] args) { ... }`
   - This is the `main` method, the entry point of the program.
   - `public`: accessible from any other class.
   - `static`: can be executed without creating an instance of the class.
   - `void`: does not return any value.
   - `main`: mandatory name for the main method.
   - `String[] args`: an array of strings to pass command-line arguments.

3. `System.out.println("Hello, World!");`
   - `System`: a predefined class providing access to system-related functionality.
   - `out`: the standard output stream.
   - `println()`: prints the text and moves to the next line.
*/
