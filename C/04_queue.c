/**
 * Queue Data Structure Implementation
 * 
 * This implementation provides a dynamic circular queue data structure using a resizable array.
 * A queue follows the FIFO (First In, First Out) principle, where elements are added at the rear
 * and removed from the front.
 * 
 * Key Features:
 * - Circular buffer: Efficiently reuses array space
 * - Dynamic resizing: Automatically grows when capacity is reached
 * - Memory efficient: Only allocates memory as needed
 * - Error handling: Proper checks for memory allocation and queue operations
 * 
 * Operations:
 * - enqueue: Adds a new element to the rear of the queue
 * - dequeue: Removes and returns the front element
 * - peek: Returns the front element without removing it
 * - isEmpty: Checks if the queue has no elements
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

// Initial capacity of the queue
#define INITIAL_CAPACITY 10

// Structure representing the queue
typedef struct {
    int* items;         // Dynamic array to store elements
    int front;          // Index of the front element
    int rear;           // Index of the rear element
    int size;           // Current number of elements
    int capacity;       // Current capacity of the array
} Queue;

// Declare queries before operations that use them to keep C17 type checking strict.
bool isEmpty(Queue* queue);

/**
 * Creates a new queue with initial capacity.
 * 
 * This function allocates memory for both the queue structure and its internal
 * array. If any memory allocation fails, the program will exit with an error
 * message. The initial capacity is set to handle 10 elements by default.
 * 
 * Returns:
 * - A pointer to the newly created queue
 * - Exits the program if memory allocation fails
 */
Queue* createQueue() {
    Queue* queue = (Queue*)malloc(sizeof(Queue));
    if (queue == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    queue->items = (int*)malloc(INITIAL_CAPACITY * sizeof(int));
    if (queue->items == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        free(queue);
        exit(EXIT_FAILURE);
    }

    queue->front = 0;
    queue->rear = -1;
    queue->size = 0;
    queue->capacity = INITIAL_CAPACITY;
    return queue;
}

/**
 * Resizes the queue when it reaches its capacity.
 * 
 * This function is called internally when the queue is full and a new element
 * needs to be added. It doubles the current capacity and copies all existing
 * elements to the new, larger array while maintaining their order. The old array
 * is freed to prevent memory leaks.
 * 
 * Parameters:
 * - queue: Pointer to the queue that needs to be resized
 */
void resizeQueue(Queue* queue) {
    int newCapacity = queue->capacity * 2;
    int* newItems = (int*)malloc(newCapacity * sizeof(int));
    
    if (newItems == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    // Copy elements to the new array
    int j = 0;
    for (int i = queue->front; j < queue->size; i = (i + 1) % queue->capacity) {
        newItems[j++] = queue->items[i];
    }

    free(queue->items);
    queue->items = newItems;
    queue->front = 0;
    queue->rear = queue->size - 1;
    queue->capacity = newCapacity;
}

/**
 * Adds a new element to the rear of the queue.
 * 
 * If the queue is full, it will automatically resize itself before adding
 * the new element. This ensures that the queue can grow indefinitely as needed.
 * The circular buffer implementation allows efficient use of the array space.
 * 
 * Parameters:
 * - queue: Pointer to the queue
 * - value: The integer value to be added to the queue
 */
void enqueue(Queue* queue, int value) {
    // Check if queue is full
    if (queue->size == queue->capacity) {
        resizeQueue(queue);
    }
    
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->items[queue->rear] = value;
    queue->size++;
}

/**
 * Removes and returns the front element from the queue.
 * 
 * This operation follows the FIFO principle, removing the oldest element
 * in the queue. If the queue is empty, the program will exit with an
 * error message.
 * 
 * Parameters:
 * - queue: Pointer to the queue
 * 
 * Returns:
 * - The value of the front element
 * - Exits the program if the queue is empty
 */
int dequeue(Queue* queue) {
    if (isEmpty(queue)) {
        fprintf(stderr, "Queue underflow\n");
        exit(EXIT_FAILURE);
    }
    
    int value = queue->items[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size--;
    return value;
}

/**
 * Returns the front element without removing it from the queue.
 * 
 * This is useful when you need to check the front element's value without
 * modifying the queue. If the queue is empty, the program will exit with
 * an error message.
 * 
 * Parameters:
 * - queue: Pointer to the queue
 * 
 * Returns:
 * - The value of the front element
 * - Exits the program if the queue is empty
 */
int peek(Queue* queue) {
    if (isEmpty(queue)) {
        fprintf(stderr, "Queue is empty\n");
        exit(EXIT_FAILURE);
    }
    return queue->items[queue->front];
}

/**
 * Checks if the queue is empty.
 * 
 * This function is used to prevent operations on an empty queue, which
 * could lead to undefined behavior.
 * 
 * Parameters:
 * - queue: Pointer to the queue
 * 
 * Returns:
 * - true if the queue has no elements
 * - false if the queue contains at least one element
 */
bool isEmpty(Queue* queue) {
    return queue->size == 0;
}

/**
 * Returns the current number of elements in the queue.
 * 
 * This function is useful for monitoring the queue's size and ensuring
 * it doesn't grow beyond expected limits.
 * 
 * Parameters:
 * - queue: Pointer to the queue
 * 
 * Returns:
 * - The number of elements currently in the queue
 */
int size(Queue* queue) {
    return queue->size;
}

/**
 * Frees all memory allocated for the queue.
 * 
 * This function should be called when the queue is no longer needed to
 * prevent memory leaks. It frees both the internal array and the queue
 * structure itself.
 * 
 * Parameters:
 * - queue: Pointer to the queue to be destroyed
 */
void destroyQueue(Queue* queue) {
    free(queue->items);
    free(queue);
}

/**
 * Example usage of the queue implementation.
 * 
 * This main function demonstrates the basic operations of the queue:
 * 1. Creating a new queue
 * 2. Adding elements (enqueue)
 * 3. Checking the size and front element
 * 4. Removing elements (dequeue)
 * 5. Proper cleanup
 */
int main() {
    Queue* queue = createQueue();
    
    // Enqueue some elements
    enqueue(queue, 10);
    enqueue(queue, 20);
    enqueue(queue, 30);
    
    printf("Queue size: %d\n", size(queue));
    printf("Front element: %d\n", peek(queue));
    
    // Dequeue elements
    while (!isEmpty(queue)) {
        printf("Dequeued: %d\n", dequeue(queue));
    }
    
    destroyQueue(queue);
    return 0;
}
