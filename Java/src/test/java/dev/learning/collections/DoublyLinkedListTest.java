package dev.learning.collections;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for DoublyLinkedList
 * This class demonstrates the usage of the DoublyLinkedList implementation
 * and tests its various operations.
 */
public class DoublyLinkedListTest {
    
    @Test
    @DisplayName("Test basic operations")
    public void testBasicOperations() {
        DoublyLinkedList<String> list = new DoublyLinkedList<>();
        
        // Test empty list
        assertTrue(list.isEmpty());
        assertEquals(0, list.size());
        assertEquals("[]", list.toString());
        
        // Test adding elements
        list.addFirst("First");
        list.addLast("Last");
        list.add(1, "Middle");
        
        assertEquals(3, list.size());
        assertEquals("[First, Middle, Last]", list.toString());
        
        // Test getting elements
        assertEquals("First", list.get(0));
        assertEquals("Middle", list.get(1));
        assertEquals("Last", list.get(2));
        
        // Test setting elements
        list.set(1, "New Middle");
        assertEquals("New Middle", list.get(1));
        
        // Test removing elements
        assertEquals("First", list.removeFirst());
        assertEquals("Last", list.removeLast());
        assertEquals(1, list.size());
        assertEquals("[New Middle]", list.toString());
    }
    
    @Test
    @DisplayName("Test edge cases")
    public void testEdgeCases() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        
        // Test adding at invalid index
        assertThrows(IndexOutOfBoundsException.class, () -> list.add(-1, 1));
        assertThrows(IndexOutOfBoundsException.class, () -> list.add(1, 1));
        
        // Test removing from empty list
        assertThrows(NoSuchElementException.class, () -> list.removeFirst());
        assertThrows(NoSuchElementException.class, () -> list.removeLast());
        
        // Test getting from empty list
        assertThrows(IndexOutOfBoundsException.class, () -> list.get(0));
        
        // Test setting in empty list
        assertThrows(IndexOutOfBoundsException.class, () -> list.set(0, 1));
    }
    
    @Test
    @DisplayName("Test complex operations")
    public void testComplexOperations() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        
        // Add elements
        for (int i = 0; i < 5; i++) {
            list.addLast(i);
        }
        
        // Test removing from middle
        assertEquals(2, list.remove(2));
        assertEquals(4, list.size());
        assertEquals("[0, 1, 3, 4]", list.toString());
        
        // Test adding in middle
        list.add(2, 2);
        assertEquals(5, list.size());
        assertEquals("[0, 1, 2, 3, 4]", list.toString());
        
        // Test clear
        list.clear();
        assertTrue(list.isEmpty());
        assertEquals(0, list.size());
        assertEquals("[]", list.toString());
    }
    
    @Test
    @DisplayName("Test performance optimization")
    public void testPerformanceOptimization() {
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        
        // Add 1000 elements
        for (int i = 0; i < 1000; i++) {
            list.addLast(i);
        }
        
        // Test accessing elements from both ends
        assertEquals(0, list.get(0));      // Access from start
        assertEquals(999, list.get(999));  // Access from end
        assertEquals(500, list.get(500));  // Access from middle
        
        // Test removing elements from both ends
        assertEquals(0, list.removeFirst());
        assertEquals(999, list.removeLast());
        assertEquals(998, list.size());
    }
} 
