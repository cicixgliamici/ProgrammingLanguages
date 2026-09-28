package dev.learning.basics;

public class StringOperations {
    public static void main(String[] args) {
        // Declare a string
        String greeting = "Hello, World!";
        
        // Concatenation
        String welcomeMessage = greeting + " Welcome to Java.";
        
        // Substring extraction
        String word = greeting.substring(7, 12); // extracts "World"
        
        // Get the length of the string
        int length = greeting.length();
        
        // Character at a specific index
        char letter = greeting.charAt(1); // 'e'
        
        // Convert to uppercase
        String upperCaseGreeting = greeting.toUpperCase();
        
        // Compare strings
        boolean isEqual = greeting.equals("Hello, World!");
        
        // Find the index of a substring
        int index = greeting.indexOf("World");
        
        // Trim whitespace
        String padded = "   Java Programming   ";
        String trimmed = padded.trim();
        
        // Split the string into an array of words
        String[] words = greeting.split(" ");
        
        // Output the results
        System.out.println("Greeting: " + greeting);
        System.out.println("Welcome Message: " + welcomeMessage);
        System.out.println("Substring (7,12): " + word);
        System.out.println("Length of greeting: " + length);
        System.out.println("Character at index 1: " + letter);
        System.out.println("Uppercase greeting: " + upperCaseGreeting);
        System.out.println("Is greeting equal to \"Hello, World!\": " + isEqual);
        System.out.println("Index of \"World\": " + index);
        System.out.println("Trimmed string: " + trimmed);
        System.out.println("Words in greeting:");
        for (String w : words) {
            System.out.println(w);
        }
    }
}

/*
Explanation:

1. `public class StringOperations { ... }`
   - Defines a public class named `StringOperations` which contains the program.

2. `public static void main(String[] args) { ... }`
   - The main method, the entry point of the program.

3. String Declaration:
   - `String greeting = "Hello, World!";`
   - Initializes a String variable with the value "Hello, World!".

4. Concatenation:
   - `String welcomeMessage = greeting + " Welcome to Java.";`
   - Combines the greeting with another string to form a welcome message.

5. Substring Extraction:
   - `String word = greeting.substring(7, 12);`
   - Extracts a part of the greeting string from index 7 to 12 (exclusive), resulting in "World".

6. Length:
   - `int length = greeting.length();`
   - Retrieves the number of characters in the greeting string.

7. Character Access:
   - `char letter = greeting.charAt(1);`
   - Gets the character at index 1 of the greeting, which is 'e'.

8. Uppercase Conversion:
   - `String upperCaseGreeting = greeting.toUpperCase();`
   - Converts all characters in the greeting to uppercase.

9. String Comparison:
   - `boolean isEqual = greeting.equals("Hello, World!");`
   - Checks if the greeting is exactly equal to the provided string.

10. Index of Substring:
    - `int index = greeting.indexOf("World");`
    - Finds the starting index of the substring "World" within the greeting.

11. Trimming Whitespace:
    - `String padded = "   Java Programming   ";`
    - `String trimmed = padded.trim();`
    - Removes leading and trailing whitespace from the string.

12. Splitting:
    - `String[] words = greeting.split(" ");`
    - Splits the greeting into an array of words using the space character as the delimiter.

13. Output:
    - `System.out.println(...)` statements print the results of the string operations to the console.
*/
