public class ArrayOperations {
    public static void main(String[] args) {
        // Declare and initialize an array of integers
        int[] numbers = {5, 10, 15, 20, 25};

        // Accessing array elements
        System.out.println("First element: " + numbers[0]);

        // Modify an element
        numbers[2] = 30;

        // Loop through the array and print each element
        System.out.println("Array elements:");
        for (int num : numbers) {
            System.out.println(num);
        }

        // Calculate the sum of all elements
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        System.out.println("Sum of array elements: " + sum);

        // Get the length of the array
        int length = numbers.length;
        System.out.println("Length of the array: " + length);

        // Sorting the array
        java.util.Arrays.sort(numbers);
        System.out.println("Sorted array:");
        for (int num : numbers) {
            System.out.println(num);
        }
    }
}

/*
Explanation:

1. `public class ArrayOperations { ... }`
   - Defines a public class named `ArrayOperations` that contains the program.

2. `public static void main(String[] args) { ... }`
   - The main method, where the program execution starts.

3. Array Declaration and Initialization:
   - `int[] numbers = {5, 10, 15, 20, 25};`
   - Declares and initializes an array of integers with specified values.

4. Accessing Array Elements:
   - `numbers[0]` accesses the first element of the array.

5. Modifying an Array Element:
   - `numbers[2] = 30;`
   - Changes the value at index 2 from 15 to 30.

6. Looping Through the Array:
   - A for-each loop iterates through each element in the array and prints it.

7. Calculating the Sum:
   - Iterates over the array to sum all elements and prints the result.

8. Array Length:
   - `int length = numbers.length;`
   - Retrieves the number of elements in the array.

9. Sorting the Array:
   - Uses `java.util.Arrays.sort(numbers);` to sort the array in ascending order.
   - Prints the sorted array.
*/
