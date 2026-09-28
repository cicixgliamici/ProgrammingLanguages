package dev.learning.collections;

/**
 * Node class for Doubly Linked List
 * Each node contains:
 * - data: the value stored in the node
 * - next: reference to the next node
 * - prev: reference to the previous node
 * 
 * @param <T> the type of data stored in the node
 */
public class Node<T> {
    private T data;
    private Node<T> next;
    private Node<T> prev;
    
    /**
     * Creates a new node with the specified data
     * @param data the data to store in the node
     */
    public Node(T data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
    
    /**
     * Gets the data stored in the node
     * @return the data
     */
    public T getData() {
        return data;
    }
    
    /**
     * Sets the data stored in the node
     * @param data the new data
     */
    public void setData(T data) {
        this.data = data;
    }
    
    /**
     * Gets the next node
     * @return the next node
     */
    public Node<T> getNext() {
        return next;
    }
    
    /**
     * Sets the next node
     * @param next the new next node
     */
    public void setNext(Node<T> next) {
        this.next = next;
    }
    
    /**
     * Gets the previous node
     * @return the previous node
     */
    public Node<T> getPrev() {
        return prev;
    }
    
    /**
     * Sets the previous node
     * @param prev the new previous node
     */
    public void setPrev(Node<T> prev) {
        this.prev = prev;
    }
    
    @Override
    public String toString() {
        return data.toString();
    }
} 
