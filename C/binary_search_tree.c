/**
 * Binary Search Tree (BST) Implementation
 *
 * A BST is a binary tree with the ordering property:
 * - For any node, all keys in the left subtree are smaller
 * - All keys in the right subtree are larger
 *
 * This implementation supports:
 * - insertion
 * - search
 * - deletion
 * - in-order traversal
 *
 * Time Complexity (average case):
 * - Search: O(log n)
 * - Insert: O(log n)
 * - Delete: O(log n)
 *
 * Worst case (unbalanced tree):
 * - O(n) for all operations
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * Structure representing a tree node.
 */
typedef struct Node {
    int key;
    struct Node* left;
    struct Node* right;
} Node;

/**
 * Creates a new BST node with the given key.
 *
 * Parameters:
 * - key: value to store in the node
 *
 * Returns:
 * - pointer to the newly allocated node
 */
Node* createNode(int key) {
    Node* node = (Node*)malloc(sizeof(Node));
    if (node == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    node->key = key;
    node->left = NULL;
    node->right = NULL;
    return node;
}

/**
 * Inserts a key into the BST.
 *
 * Parameters:
 * - root: root of the BST (can be NULL)
 * - key: value to insert
 *
 * Returns:
 * - updated root of the BST
 */
Node* insert(Node* root, int key) {
    if (root == NULL) {
        return createNode(key);
    }

    if (key < root->key) {
        root->left = insert(root->left, key);
    } else if (key > root->key) {
        root->right = insert(root->right, key);
    }
    // Duplicate keys are ignored to keep the tree strict
    return root;
}

/**
 * Searches for a key in the BST.
 *
 * Parameters:
 * - root: root of the BST
 * - key: value to search for
 *
 * Returns:
 * - true if found
 * - false otherwise
 */
bool search(Node* root, int key) {
    if (root == NULL) {
        return false;
    }
    if (root->key == key) {
        return true;
    }
    if (key < root->key) {
        return search(root->left, key);
    }
    return search(root->right, key);
}

/**
 * Finds the node with the smallest key in a subtree.
 *
 * Parameters:
 * - node: root of the subtree
 *
 * Returns:
 * - pointer to the node with the minimum key
 */
Node* findMin(Node* node) {
    Node* current = node;
    while (current != NULL && current->left != NULL) {
        current = current->left;
    }
    return current;
}

/**
 * Deletes a key from the BST.
 *
 * Deletion cases:
 * 1. Node is a leaf -> remove it
 * 2. Node has one child -> replace node with child
 * 3. Node has two children -> replace with in-order successor
 *
 * Parameters:
 * - root: root of the BST
 * - key: value to delete
 *
 * Returns:
 * - updated root of the BST
 */
Node* delete(Node* root, int key) {
    if (root == NULL) {
        return NULL;
    }

    if (key < root->key) {
        root->left = delete(root->left, key);
    } else if (key > root->key) {
        root->right = delete(root->right, key);
    } else {
        // Node found
        if (root->left == NULL) {
            Node* rightChild = root->right;
            free(root);
            return rightChild;
        }
        if (root->right == NULL) {
            Node* leftChild = root->left;
            free(root);
            return leftChild;
        }

        // Node with two children: replace with in-order successor
        Node* successor = findMin(root->right);
        root->key = successor->key;
        root->right = delete(root->right, successor->key);
    }

    return root;
}

/**
 * Performs in-order traversal (left, root, right).
 *
 * Parameters:
 * - root: root of the BST
 */
void inorderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    inorderTraversal(root->left);
    printf("%d ", root->key);
    inorderTraversal(root->right);
}

/**
 * Frees all nodes in the BST.
 *
 * Parameters:
 * - root: root of the BST
 */
void destroyTree(Node* root) {
    if (root == NULL) {
        return;
    }
    destroyTree(root->left);
    destroyTree(root->right);
    free(root);
}

/**
 * Example usage of the BST implementation.
 */
int main(void) {
    Node* root = NULL;

    // Insert values
    int values[] = {50, 30, 70, 20, 40, 60, 80};
    int size = (int)(sizeof(values) / sizeof(values[0]));
    for (int i = 0; i < size; i++) {
        root = insert(root, values[i]);
    }

    printf("In-order traversal: ");
    inorderTraversal(root);
    printf("\n");

    // Search for a value
    int target = 60;
    printf("Search %d: %s\n", target, search(root, target) ? "found" : "not found");

    // Delete a value and show updated traversal
    root = delete(root, 30);
    printf("After deleting 30: ");
    inorderTraversal(root);
    printf("\n");

    destroyTree(root);
    return 0;
}
