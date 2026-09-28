package dev.learning.collections;

import java.util.NoSuchElementException;

/**
 * Implementation of a Doubly Linked List data structure
 * This class provides various operations for manipulating a doubly linked list
 * including insertion, deletion, traversal, and searching.
 * 
 * @param <T> the type of elements stored in the list
 */
public class DoublyLinkedList<T> {
    private Node<T> head;
    private Node<T> tail;
    private int size;
    
    /**
     * Creates an empty doubly linked list
     */
    public DoublyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }
    
    /**
     * Adds an element at the beginning of the list
     * @param data the element to add
     */
    public void addFirst(T data) {
        Node<T> newNode = new Node<>(data);
        if (isEmpty()) {
            head = tail = newNode;
        } else {
            newNode.setNext(head);
            head.setPrev(newNode);
            head = newNode;
        }
        size++;
    }
    
    /**
     * Adds an element at the end of the list
     * @param data the element to add
     */
    public void addLast(T data) {
        Node<T> newNode = new Node<>(data);
        if (isEmpty()) {
            head = tail = newNode;
        } else {
            newNode.setPrev(tail);
            tail.setNext(newNode);
            tail = newNode;
        }
        size++;
    }
    
    /**
     * Adds an element at the specified index
     * @param index the position to insert the element
     * @param data the element to add
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public void add(int index, T data) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        
        if (index == 0) {
            addFirst(data);
            return;
        }
        
        if (index == size) {
            addLast(data);
            return;
        }
        
        Node<T> current = getNode(index);
        Node<T> newNode = new Node<>(data);
        
        newNode.setPrev(current.getPrev());
        newNode.setNext(current);
        current.getPrev().setNext(newNode);
        current.setPrev(newNode);
        
        size++;
    }
    
    /**
     * Removes the first element from the list
     * @return the removed element
     * @throws NoSuchElementException if the list is empty
     */
    public T removeFirst() {
        if (isEmpty()) {
            throw new NoSuchElementException("List is empty");
        }
        
        T data = head.getData();
        head = head.getNext();
        
        if (head == null) {
            tail = null;
        } else {
            head.setPrev(null);
        }
        
        size--;
        return data;
    }
    
    /**
     * Removes the last element from the list
     * @return the removed element
     * @throws NoSuchElementException if the list is empty
     */
    public T removeLast() {
        if (isEmpty()) {
            throw new NoSuchElementException("List is empty");
        }
        
        T data = tail.getData();
        tail = tail.getPrev();
        
        if (tail == null) {
            head = null;
        } else {
            tail.setNext(null);
        }
        
        size--;
        return data;
    }
    
    /**
     * Removes the element at the specified index
     * @param index the position of the element to remove
     * @return the removed element
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public T remove(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        
        if (index == 0) {
            return removeFirst();
        }
        
        if (index == size - 1) {
            return removeLast();
        }
        
        Node<T> current = getNode(index);
        T data = current.getData();
        
        current.getPrev().setNext(current.getNext());
        current.getNext().setPrev(current.getPrev());
        
        size--;
        return data;
    }
    
    /**
     * Gets the element at the specified index
     * @param index the position of the element
     * @return the element at the specified position
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public T get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        return getNode(index).getData();
    }
    
    /**
     * Sets the element at the specified index
     * @param index the position of the element to set
     * @param data the new element
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public void set(int index, T data) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        getNode(index).setData(data);
    }
    
    /**
     * Returns the number of elements in the list
     * @return the size of the list
     */
    public int size() {
        return size;
    }
    
    /**
     * Checks if the list is empty
     * @return true if the list is empty, false otherwise
     */
    public boolean isEmpty() {
        return size == 0;
    }
    
    /**
     * Clears all elements from the list
     */
    public void clear() {
        head = null;
        tail = null;
        size = 0;
    }
    
    /**
     * Returns a string representation of the list
     * @return a string containing all elements in the list
     */
    @Override
    public String toString() {
        if (isEmpty()) {
            return "[]";
        }
        
        StringBuilder sb = new StringBuilder("[");
        Node<T> current = head;
        
        while (current != null) {
            sb.append(current.getData());
            if (current.getNext() != null) {
                sb.append(", ");
            }
            current = current.getNext();
        }
        
        sb.append("]");
        return sb.toString();
    }
    
    /**
     * Gets the node at the specified index
     * @param index the position of the node
     * @return the node at the specified position
     */
    private Node<T> getNode(int index) {
        Node<T> current;
        if (index < size / 2) {
            current = head;
            for (int i = 0; i < index; i++) {
                current = current.getNext();
            }
        } else {
            current = tail;
            for (int i = size - 1; i > index; i--) {
                current = current.getPrev();
            }
        }
        return current;
    }
} 
