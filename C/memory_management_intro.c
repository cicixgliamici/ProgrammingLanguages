/**
 * Introduction to Memory Management in C
 *
 * C gives you direct control over memory. Understanding how memory works
 * is essential to avoid leaks, crashes, and undefined behavior.
 *
 * This example demonstrates:
 * - Stack vs Heap memory
 * - Dynamic allocation with malloc/calloc/realloc
 * - Proper deallocation with free
 * - Common mistakes to avoid
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Demonstrates stack allocation.
 *
 * Stack variables are automatically created and destroyed when the function
 * is entered/exited. They are fast to allocate but have limited size.
 */
void stackExample(void) {
    int number = 42;              // Stored on the stack
    char message[] = "Hello";     // Also on the stack

    printf("Stack number: %d\n", number);
    printf("Stack message: %s\n", message);
}

/**
 * Demonstrates heap allocation with malloc.
 *
 * Heap memory must be explicitly allocated and freed by the programmer.
 * malloc allocates a raw block of bytes and does NOT initialize it.
 */
void heapExampleMalloc(void) {
    int *numbers = (int *)malloc(5 * sizeof(int));
    if (numbers == NULL) {
        fprintf(stderr, "malloc failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < 5; i++) {
        numbers[i] = (i + 1) * 10;
    }

    printf("Heap values (malloc): ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    free(numbers);
}

/**
 * Demonstrates heap allocation with calloc.
 *
 * calloc allocates and initializes the memory to zero.
 */
void heapExampleCalloc(void) {
    int *numbers = (int *)calloc(5, sizeof(int));
    if (numbers == NULL) {
        fprintf(stderr, "calloc failed\n");
        exit(EXIT_FAILURE);
    }

    printf("Heap values (calloc, zero-initialized): ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    free(numbers);
}

/**
 * Demonstrates resizing memory with realloc.
 *
 * realloc changes the size of an existing allocation. It may move the block,
 * so the returned pointer must be used afterwards.
 */
void heapExampleRealloc(void) {
    int *numbers = (int *)malloc(3 * sizeof(int));
    if (numbers == NULL) {
        fprintf(stderr, "malloc failed\n");
        exit(EXIT_FAILURE);
    }

    numbers[0] = 1;
    numbers[1] = 2;
    numbers[2] = 3;

    int *resized = (int *)realloc(numbers, 6 * sizeof(int));
    if (resized == NULL) {
        free(numbers);
        fprintf(stderr, "realloc failed\n");
        exit(EXIT_FAILURE);
    }

    // Initialize new elements
    for (int i = 3; i < 6; i++) {
        resized[i] = (i + 1) * 10;
    }

    printf("Heap values (realloc): ");
    for (int i = 0; i < 6; i++) {
        printf("%d ", resized[i]);
    }
    printf("\n");

    free(resized);
}

/**
 * Demonstrates safe string duplication using malloc and strcpy.
 *
 * Always allocate enough space for the null terminator.
 */
void stringDupExample(void) {
    const char *source = "Memory management in C";
    size_t length = strlen(source) + 1;

    char *copy = (char *)malloc(length * sizeof(char));
    if (copy == NULL) {
        fprintf(stderr, "malloc failed\n");
        exit(EXIT_FAILURE);
    }

    strcpy(copy, source);
    printf("Copied string: %s\n", copy);

    free(copy);
}

/**
 * Entry point to run all examples.
 */
int main(void) {
    printf("== Stack example ==\n");
    stackExample();

    printf("\n== Heap example (malloc) ==\n");
    heapExampleMalloc();

    printf("\n== Heap example (calloc) ==\n");
    heapExampleCalloc();

    printf("\n== Heap example (realloc) ==\n");
    heapExampleRealloc();

    printf("\n== Heap example (string copy) ==\n");
    stringDupExample();

    return 0;
}
