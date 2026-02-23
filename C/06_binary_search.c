/**
 * Binary Search Algorithm (Iterative and Recursive)
 *
 * Binary search efficiently finds a target value inside a sorted array by
 * repeatedly dividing the search interval in half.
 *
 * Preconditions:
 * - The input array MUST be sorted in ascending order.
 *
 * Time Complexity:
 * - Best: O(1) (target found at the middle)
 * - Worst: O(log n)
 *
 * Space Complexity:
 * - Iterative: O(1)
 * - Recursive: O(log n) due to call stack
 */

#include <stdio.h>

/**
 * Performs binary search iteratively.
 *
 * Parameters:
 * - arr: pointer to the first element of the sorted array
 * - size: number of elements in the array
 * - target: value to search for
 *
 * Returns:
 * - index of the target if found
 * - -1 if the target is not present
 */
int binarySearchIterative(const int *arr, int size, int target) {
    int left = 0;
    int right = size - 1;

    while (left <= right) {
        // Prevent potential overflow: (left + right) / 2
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

/**
 * Performs binary search recursively.
 *
 * Parameters:
 * - arr: pointer to the first element of the sorted array
 * - left: left boundary index of the current search interval
 * - right: right boundary index of the current search interval
 * - target: value to search for
 *
 * Returns:
 * - index of the target if found
 * - -1 if the target is not present
 */
int binarySearchRecursive(const int *arr, int left, int right, int target) {
    if (left > right) {
        return -1;
    }

    int mid = left + (right - left) / 2;

    if (arr[mid] == target) {
        return mid;
    }
    if (arr[mid] < target) {
        return binarySearchRecursive(arr, mid + 1, right, target);
    }

    return binarySearchRecursive(arr, left, mid - 1, target);
}

/**
 * Example usage of binary search.
 */
int main(void) {
    int numbers[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int size = (int)(sizeof(numbers) / sizeof(numbers[0]));
    int target = 23;

    int iterativeIndex = binarySearchIterative(numbers, size, target);
    int recursiveIndex = binarySearchRecursive(numbers, 0, size - 1, target);

    printf("Iterative search: target %d found at index %d\n", target, iterativeIndex);
    printf("Recursive search: target %d found at index %d\n", target, recursiveIndex);

    return 0;
}
