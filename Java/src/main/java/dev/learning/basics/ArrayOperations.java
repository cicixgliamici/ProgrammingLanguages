package dev.learning.basics;

public class ArrayOperations {
    public static void main(String[] args) {
        // 1. Declaration and initialization of an array of integers
        int[] numbers = {5, 10, 15, 20, 25};

        // 2. Accessing an element of the array
        System.out.println("First element: " + numbers[0]);

        // 3. Modifying an element of the array
        numbers[2] = 30; // Changes the value at index 2 from 15 to 30

        // 4. Iterating over the array using a for-each loop and printing each element
        System.out.println("Array elements:");
        for (int num : numbers) {
            System.out.println(num);
        }

        // 5. Calculating the sum of all array elements
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        System.out.println("Sum of array elements: " + sum);

        // 6. Getting the length of the array
        int length = numbers.length;
        System.out.println("Length of the array: " + length);

        // 7. Sorting the array in ascending order using Arrays.sort()
        java.util.Arrays.sort(numbers);
        System.out.println("Sorted array:");
        for (int num : numbers) {
            System.out.println(num);
        }

        // ---------------------------------------------------------
        // Additional array operations using java.util.Arrays
        // ---------------------------------------------------------

        // 8. Arrays.toString(): Converts the array to a String for quick visualization
        System.out.println("Array as String: " + java.util.Arrays.toString(numbers));

        // 9. Arrays.copyOf(): Creates a copy of the array
        int[] copyNumbers = java.util.Arrays.copyOf(numbers, numbers.length);
        System.out.println("Copied array: " + java.util.Arrays.toString(copyNumbers));

        // 10. Arrays.equals(): Compares two arrays to check if they are equal
        boolean isEqual = java.util.Arrays.equals(numbers, copyNumbers);
        System.out.println("Are the original and copied arrays equal? " + isEqual);

        // 11. Arrays.fill(): Fills an array with a specific value
        int[] filledArray = new int[5];
        java.util.Arrays.fill(filledArray, 100);
        System.out.println("Array filled with 100: " + java.util.Arrays.toString(filledArray));

        // 12. Arrays.binarySearch(): Searches for a value in a sorted array
        // The array must be sorted before using binarySearch
        int index = java.util.Arrays.binarySearch(numbers, 20);
        if (index >= 0) {
            System.out.println("Element 20 found at index: " + index);
        } else {
            System.out.println("Element 20 not found. Insertion point: " + (-index - 1));
        }

        // 13. Arrays.parallelSort(): Sorts the array using a parallel sorting algorithm
        // Creating a new unsorted array to demonstrate parallelSort
        int[] unsortedNumbers = {25, 5, 15, 10, 20};
        System.out.println("Unsorted array: " + java.util.Arrays.toString(unsortedNumbers));
        java.util.Arrays.parallelSort(unsortedNumbers);
        System.out.println("Array sorted with parallelSort: " + java.util.Arrays.toString(unsortedNumbers));

        // 14. Arrays.setAll(): Sets all elements of an array using a lambda expression
        // In this example, each element is set to (index * 10)
        int[] setAllArray = new int[5];
        java.util.Arrays.setAll(setAllArray, i -> i * 10);
        System.out.println("Array after setAll: " + java.util.Arrays.toString(setAllArray));

        // 15. Arrays.stream(): Creates a stream from the array for functional operations
        // Example: Calculating the average of the array elements
        double average = java.util.Arrays.stream(numbers).average().orElse(0);
        System.out.println("Average of array elements: " + average);
    }
}

/*
Additional Explanation:

8. Arrays.toString(array)
   - Converts the array to a formatted string, making it easy to print the entire array on one line.

9. Arrays.copyOf(original, newLength)
   - Creates a copy of the original array. This can be used to clone the array or create a new array with a different length.

10. Arrays.equals(array1, array2)
    - Compares two arrays to check if they contain the same elements in the same order.

11. Arrays.fill(array, value)
    - Fills every element of the array with the specified value.

12. Arrays.binarySearch(array, key)
    - Searches for a specific element in the sorted array. Returns the index if found,
      otherwise returns a negative value indicating the insertion point.

13. Arrays.parallelSort(array)
    - Sorts the array using parallelism, which can improve performance on large arrays.

14. Arrays.setAll(array, lambda)
    - Sets each element of the array based on a lambda function that takes the index and returns the value.

15. Arrays.stream(array)
    - Creates a stream from the array, enabling functional operations such as filter, map, reduce, and average.
*/
