import java.util.Arrays;
import java.util.Random;

/**
 * A utility class that implements various array algorithms including:
 * - Different sorting algorithms (Bubble, Selection, Insertion, Quick, Merge)
 * - Binary search
 * - Array operations (shuffle, reverse, find min/max)
 * 
 * This class serves as a demonstration of common array algorithms and their implementations.
 * Each algorithm is implemented with detailed comments explaining its working principle,
 * time and space complexity, and important implementation details.
 */
public class ArrayAlgorithms {
    
    /**
     * Sorts an array using Bubble Sort algorithm
     * 
     * Working Principle:
     * - Repeatedly steps through the array, compares adjacent elements and swaps them if they are in wrong order
     * - After each pass, the largest unsorted element "bubbles up" to its correct position
     * - Uses a boolean flag to optimize the algorithm by stopping if no swaps occur in a pass
     * 
     * Time Complexity: O(n²) in worst and average case, O(n) in best case (when array is already sorted)
     * Space Complexity: O(1) as it sorts in-place
     * 
     * @param arr the array to be sorted
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            // Last i elements are already in place
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap elements if they are in wrong order
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            // If no swapping occurred in this pass, array is sorted
            if (!swapped) break;
        }
    }
    
    /**
     * Sorts an array using Selection Sort algorithm
     * 
     * Working Principle:
     * - Divides the array into a sorted and unsorted region
     * - Repeatedly selects the smallest element from the unsorted region
     * - Places it at the beginning of the unsorted region
     * - The sorted region grows from left to right
     * 
     * Time Complexity: O(n²) in all cases (best, average, worst)
     * Space Complexity: O(1) as it sorts in-place
     * 
     * @param arr the array to be sorted
     */
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            // Find the minimum element in unsorted array
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            // Swap the found minimum element with the first element
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
        }
    }
    
    /**
     * Sorts an array using Insertion Sort algorithm
     * 
     * Working Principle:
     * - Builds the sorted array one element at a time
     * - Takes each element and inserts it into its correct position in the sorted portion
     * - Efficient for small arrays and nearly sorted arrays
     * - Similar to how we sort playing cards in our hands
     * 
     * Time Complexity: O(n²) in worst and average case, O(n) in best case (when array is already sorted)
     * Space Complexity: O(1) as it sorts in-place
     * 
     * @param arr the array to be sorted
     */
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];  // Current element to be inserted
            int j = i - 1;     // Index of last element in sorted portion
            
            // Move elements greater than key one position ahead
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;  // Insert key in its correct position
        }
    }
    
    /**
     * Sorts an array using Quick Sort algorithm
     * 
     * Working Principle:
     * - Uses divide-and-conquer strategy
     * - Picks a 'pivot' element and partitions the array around it
     * - Elements smaller than pivot go to left, larger to right
     * - Recursively sorts the sub-arrays
     * 
     * Time Complexity: O(n log n) average case, O(n²) worst case (when array is already sorted)
     * Space Complexity: O(log n) due to recursion stack
     * 
     * @param arr the array to be sorted
     */
    public static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }
    
    private static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // Get the partition index
            int pi = partition(arr, low, high);
            
            // Recursively sort elements before and after partition
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
    
    private static int partition(int[] arr, int low, int high) {
        // Choose the rightmost element as pivot
        int pivot = arr[high];
        int i = low - 1;  // Index of smaller element
        
        for (int j = low; j < high; j++) {
            // If current element is smaller than or equal to pivot
            if (arr[j] <= pivot) {
                i++;
                // Swap elements
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        
        // Place pivot in its correct position
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        
        return i + 1;
    }
    
    /**
     * Sorts an array using Merge Sort algorithm
     * 
     * Working Principle:
     * - Uses divide-and-conquer strategy
     * - Divides array into two halves, recursively sorts them
     * - Merges the sorted halves to produce final sorted array
     * - Stable sort (maintains relative order of equal elements)
     * 
     * Time Complexity: O(n log n) in all cases
     * Space Complexity: O(n) for temporary arrays
     * 
     * @param arr the array to be sorted
     */
    public static void mergeSort(int[] arr) {
        if (arr.length <= 1) return;
        
        // Divide array into two halves
        int mid = arr.length / 2;
        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, arr.length);
        
        // Recursively sort the two halves
        mergeSort(left);
        mergeSort(right);
        
        // Merge the sorted halves
        merge(arr, left, right);
    }
    
    private static void merge(int[] arr, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;
        
        // Compare and merge elements from both arrays
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }
        
        // Copy remaining elements of left array
        while (i < left.length) {
            arr[k++] = left[i++];
        }
        
        // Copy remaining elements of right array
        while (j < right.length) {
            arr[k++] = right[j++];
        }
    }
    
    /**
     * Searches for a value in a sorted array using Binary Search
     * 
     * Working Principle:
     * - Requires array to be sorted
     * - Repeatedly divides the search interval in half
     * - Compares target value with middle element
     * - Eliminates half of the remaining elements in each step
     * 
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     * 
     * @param arr the sorted array to search in
     * @param target the value to search for
     * @return the index of the target value, or -1 if not found
     */
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            // Calculate middle index (prevents integer overflow)
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) {
                return mid;
            }
            
            // If target is greater, ignore left half
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                // If target is smaller, ignore right half
                right = mid - 1;
            }
        }
        
        return -1;  // Element not found
    }
    
    /**
     * Shuffles an array using Fisher-Yates algorithm
     * 
     * Working Principle:
     * - Generates a random permutation of the array
     * - Iterates through array from end to start
     * - Swaps each element with a random element from the remaining unshuffled portion
     * - Ensures unbiased random permutation
     * 
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     * 
     * @param arr the array to be shuffled
     */
    public static void shuffle(int[] arr) {
        Random random = new Random();
        for (int i = arr.length - 1; i > 0; i--) {
            // Generate random index between 0 and i (inclusive)
            int j = random.nextInt(i + 1);
            // Swap elements
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    
    /**
     * Reverses an array in-place
     * 
     * Working Principle:
     * - Uses two pointers (left and right)
     * - Swaps elements from both ends moving towards the center
     * - Continues until pointers meet in the middle
     * 
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     * 
     * @param arr the array to be reversed
     */
    public static void reverse(int[] arr) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left < right) {
            // Swap elements from both ends
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
    
    /**
     * Finds the minimum value in an array
     * 
     * Working Principle:
     * - Initializes min with first element
     * - Compares each element with current min
     * - Updates min if a smaller element is found
     * 
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     * 
     * @param arr the array to search in
     * @return the minimum value
     * @throws IllegalArgumentException if array is empty
     */
    public static int findMin(int[] arr) {
        if (arr.length == 0) {
            throw new IllegalArgumentException("Array is empty");
        }
        
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }
    
    /**
     * Finds the maximum value in an array
     * 
     * Working Principle:
     * - Initializes max with first element
     * - Compares each element with current max
     * - Updates max if a larger element is found
     * 
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     * 
     * @param arr the array to search in
     * @return the maximum value
     * @throws IllegalArgumentException if array is empty
     */
    public static int findMax(int[] arr) {
        if (arr.length == 0) {
            throw new IllegalArgumentException("Array is empty");
        }
        
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }
    
    /**
     * Main method demonstrating the usage of various algorithms
     * 
     * This method creates a test array and demonstrates:
     * - Different sorting algorithms
     * - Binary search
     * - Array operations (shuffle, reverse)
     * - Finding minimum and maximum values
     */
    public static void main(String[] args) {
        // Create a test array
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("Original array: " + Arrays.toString(arr));
        
        // Test different sorting algorithms
        int[] bubbleArr = arr.clone();
        bubbleSort(bubbleArr);
        System.out.println("Bubble Sort: " + Arrays.toString(bubbleArr));
        
        int[] selectionArr = arr.clone();
        selectionSort(selectionArr);
        System.out.println("Selection Sort: " + Arrays.toString(selectionArr));
        
        int[] insertionArr = arr.clone();
        insertionSort(insertionArr);
        System.out.println("Insertion Sort: " + Arrays.toString(insertionArr));
        
        int[] quickArr = arr.clone();
        quickSort(quickArr);
        System.out.println("Quick Sort: " + Arrays.toString(quickArr));
        
        int[] mergeArr = arr.clone();
        mergeSort(mergeArr);
        System.out.println("Merge Sort: " + Arrays.toString(mergeArr));
        
        // Test binary search
        int target = 25;
        int index = binarySearch(mergeArr, target);
        System.out.println("Binary Search for " + target + ": " + index);
        
        // Test array operations
        shuffle(arr);
        System.out.println("Shuffled array: " + Arrays.toString(arr));
        
        reverse(arr);
        System.out.println("Reversed array: " + Arrays.toString(arr));
        
        System.out.println("Minimum value: " + findMin(arr));
        System.out.println("Maximum value: " + findMax(arr));
    }
} 