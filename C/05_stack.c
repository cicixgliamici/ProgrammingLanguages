/**
 * Stack Data Structure Implementation
 * 
 * This implementation provides a dynamic stack data structure using a resizable array.
 * A stack follows the LIFO (Last In, First Out) principle, where elements are added
 * and removed from the same end (the top).
 * 
 * Key Features:
 * - Dynamic resizing: The stack automatically grows when it reaches capacity
 * - Memory efficient: Only allocates memory as needed
 * - Error handling: Proper checks for memory allocation and stack operations
 * 
 * Operations:
 * - push: Adds a new element to the top of the stack
 * - pop: Removes and returns the top element
 * - peek: Returns the top element without removing it
 * - isEmpty: Checks if the stack has no elements
 * - size: Returns the current number of elements
 * 
 * Memory Management:
 * - All memory is properly allocated and freed
 * - Automatic resizing when capacity is reached
 * - Cleanup function to prevent memory leaks
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Initial capacity of the stack
#define INITIAL_CAPACITY 10

// Structure representing the stack
typedef struct {
    int* items;         // Dynamic array to store elements
    int top;            // Index of the top element
    int capacity;       // Current capacity of the array
} Stack;

/**
 * Creates a new stack with initial capacity.
 * 
 * This function allocates memory for both the stack structure and its internal
 * array. If any memory allocation fails, the program will exit with an error
 * message. The initial capacity is set to handle 10 elements by default.
 * 
 * Returns:
 * - A pointer to the newly created stack
 * - Exits the program if memory allocation fails
 */
Stack* createStack() {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    if (stack == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    stack->items = (int*)malloc(INITIAL_CAPACITY * sizeof(int));
    if (stack->items == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        free(stack);
        exit(EXIT_FAILURE);
    }

    stack->top = -1;  // Stack is empty
    stack->capacity = INITIAL_CAPACITY;
    return stack;
}

/**
 * Resizes the stack when it reaches its capacity.
 * 
 * This function is called internally when the stack is full and a new element
 * needs to be added. It doubles the current capacity and copies all existing
 * elements to the new, larger array. The old array is freed to prevent memory leaks.
 * 
 * Parameters:
 * - stack: Pointer to the stack that needs to be resized
 */
void resizeStack(Stack* stack) {
    int newCapacity = stack->capacity * 2;
    int* newItems = (int*)realloc(stack->items, newCapacity * sizeof(int));
    
    if (newItems == NULL) {
        fprintf(stderr, "Memory reallocation failed\n");
        exit(EXIT_FAILURE);
    }

    stack->items = newItems;
    stack->capacity = newCapacity;
}

/**
 * Adds a new element to the top of the stack.
 * 
 * If the stack is full, it will automatically resize itself before adding
 * the new element. This ensures that the stack can grow indefinitely as needed.
 * 
 * Parameters:
 * - stack: Pointer to the stack
 * - value: The integer value to be added to the stack
 */
void push(Stack* stack, int value) {
    // Check if stack is full
    if (stack->top == stack->capacity - 1) {
        resizeStack(stack);
    }
    
    stack->items[++stack->top] = value;
}

/**
 * Removes and returns the top element from the stack.
 * 
 * This operation follows the LIFO principle, removing the most recently
 * added element. If the stack is empty, the program will exit with an
 * error message.
 * 
 * Parameters:
 * - stack: Pointer to the stack
 * 
 * Returns:
 * - The value of the top element
 * - Exits the program if the stack is empty
 */
int pop(Stack* stack) {
    if (isEmpty(stack)) {
        fprintf(stderr, "Stack underflow\n");
        exit(EXIT_FAILURE);
    }
    return stack->items[stack->top--];
}

/**
 * Returns the top element without removing it from the stack.
 * 
 * This is useful when you need to check the top element's value without
 * modifying the stack. If the stack is empty, the program will exit with
 * an error message.
 * 
 * Parameters:
 * - stack: Pointer to the stack
 * 
 * Returns:
 * - The value of the top element
 * - Exits the program if the stack is empty
 */
int peek(Stack* stack) {
    if (isEmpty(stack)) {
        fprintf(stderr, "Stack is empty\n");
        exit(EXIT_FAILURE);
    }
    return stack->items[stack->top];
}

/**
 * Checks if the stack is empty.
 * 
 * This function is used to prevent operations on an empty stack, which
 * could lead to undefined behavior.
 * 
 * Parameters:
 * - stack: Pointer to the stack
 * 
 * Returns:
 * - true if the stack has no elements
 * - false if the stack contains at least one element
 */
bool isEmpty(Stack* stack) {
    return stack->top == -1;
}

/**
 * Returns the current number of elements in the stack.
 * 
 * This function is useful for monitoring the stack's size and ensuring
 * it doesn't grow beyond expected limits.
 * 
 * Parameters:
 * - stack: Pointer to the stack
 * 
 * Returns:
 * - The number of elements currently in the stack
 */
int size(Stack* stack) {
    return stack->top + 1;
}

/**
 * Frees all memory allocated for the stack.
 * 
 * This function should be called when the stack is no longer needed to
 * prevent memory leaks. It frees both the internal array and the stack
 * structure itself.
 * 
 * Parameters:
 * - stack: Pointer to the stack to be destroyed
 */
void destroyStack(Stack* stack) {
    free(stack->items);
    free(stack);
}

/**
 * Example usage of the stack implementation.
 * 
 * This main function demonstrates the basic operations of the stack:
 * 1. Creating a new stack
 * 2. Adding elements (push)
 * 3. Checking the size and top element
 * 4. Removing elements (pop)
 * 5. Proper cleanup
 */
int main() {
    Stack* stack = createStack();
    
    // Push some elements
    push(stack, 10);
    push(stack, 20);
    push(stack, 30);
    
    printf("Stack size: %d\n", size(stack));
    printf("Top element: %d\n", peek(stack));
    
    // Pop elements
    while (!isEmpty(stack)) {
        printf("Popped: %d\n", pop(stack));
    }
    
    destroyStack(stack);
    return 0;
} 