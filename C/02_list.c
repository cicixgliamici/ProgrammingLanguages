#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> // For bool type in search functions

// Node structure for linked list
struct node {
    int value;         // Data stored in the node
    struct node *next; // Pointer to next node
};

/***********************************************
 * FUNDAMENTAL LINKED LIST OPERATIONS          *
 * (with time complexity explanations)         *
 ***********************************************/

// Print all elements in the list (Complexity: O(n))
void printLinkedList(struct node *head) {
    printf("List: ");
    while (head != NULL) {
        printf("%d ", head->value);
        head = head->next; // Move to next node
    }
    printf("\n");
}

// Insert at head (Complexity: O(1))
struct node* insertAtHead(struct node *head, int value) {
    struct node *newNode = malloc(sizeof(struct node));
    newNode->value = value;
    newNode->next = head; // New node points to old head
    return newNode; // Return new head
}

// Insert at tail (Complexity: O(n))
struct node* insertAtTail(struct node *head, int value) {
    struct node *newNode = malloc(sizeof(struct node));
    newNode->value = value;
    newNode->next = NULL;

    // If list is empty
    if (head == NULL) return newNode;

    // Traverse to last node
    struct node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    return head;
}

// Delete node by value (Complexity: O(n))
struct node* deleteNode(struct node *head, int value) {
    if (head == NULL) return NULL;

    // Special case: delete head
    if (head->value == value) {
        struct node *temp = head->next;
        free(head);
        return temp;
    }

    struct node *current = head;
    while (current->next != NULL) {
        if (current->next->value == value) {
            struct node *temp = current->next;
            current->next = temp->next;
            free(temp);
            return head;
        }
        current = current->next;
    }
    return head;
}

// Search for value (Complexity: O(n))
bool searchNode(struct node *head, int value) {
    while (head != NULL) {
        if (head->value == value) return true;
        head = head->next;
    }
    return false;
}

// Get list length (Complexity: O(n))
int getLength(struct node *head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}

// Free entire list (Complexity: O(n))
void freeList(struct node *head) {
    struct node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main() {
    // Create initial list 1->2->3->NULL
    struct node *head = NULL;
    
    // Build list using insertions
    head = insertAtHead(head, 2);
    head = insertAtHead(head, 1);
    head = insertAtTail(head, 3);
    head = insertAtTail(head, 4);
    
    printLinkedList(head); // List: 1 2 3 4 
    
    // Demonstrate deletions
    head = deleteNode(head, 2);
    head = deleteNode(head, 4);
    printLinkedList(head); // List: 1 3 
    
    // Demonstrate search
    printf("Search 3: %s\n", searchNode(head, 3) ? "Found" : "Not found");
    
    // Show length
    printf("List length: %d\n", getLength(head));
    
    // Clean up memory
    freeList(head);
    
    return 0;
}


/*
 * Key Concepts Explained:
 *
 * Node Structure:
 * - Contains value (data storage)
 * - next pointer (links to next node)
 * - Last node points to NULL
 *
 * Time Complexities:
 * - O(1): Insert/delete at head
 * - O(n): Insert/delete at tail, search, access by index
 * - O(n): All operations requiring traversal
 *
 * Memory Management:
 * - Always free() deleted nodes
 * - freeList() is essential to prevent memory leaks
 * - Dynamic allocation using malloc()
 *
 * Common Operations:
 * - Insertion: Create node and adjust pointers
 * - Deletion: Adjust pointers then free memory
 * - Traversal: Use temporary pointer to iterate
 *
 * Edge Cases:
 * - Handle empty list and head/tail operations carefully
 *
 * Advantages over Arrays:
 * - Dynamic size
 * - Efficient insertions/deletions
 * - No wasted memory
 *
 * Disadvantages:
 * - No random access
 * - Extra memory for pointers
 * - Cache-unfriendly
 *
 * This implementation demonstrates fundamental linked list operations 
 * with proper memory management. Each function shows typical patterns 
 * used in list manipulation, and the complexity comments help understand 
 * algorithm efficiency.
 */
