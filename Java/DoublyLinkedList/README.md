# Doubly Linked List Implementation

This project demonstrates a complete implementation of a Doubly Linked List data structure in Java. It includes comprehensive testing and documentation.

## What is a Doubly Linked List?

A doubly linked list is a linear data structure where each node contains:
- Data
- A reference to the next node
- A reference to the previous node

This allows for:
- Traversal in both directions
- Efficient insertion and deletion at both ends
- O(1) access to both head and tail

## Features

The implementation includes:
- Generic type support (`<T>`)
- Basic operations (add, remove, get, set)
- Edge case handling
- Performance optimizations
- Comprehensive testing

## Operations

### Basic Operations
- `addFirst(T data)`: Add element at the beginning
- `addLast(T data)`: Add element at the end
- `add(int index, T data)`: Add element at specified position
- `removeFirst()`: Remove first element
- `removeLast()`: Remove last element
- `remove(int index)`: Remove element at specified position
- `get(int index)`: Get element at specified position
- `set(int index, T data)`: Set element at specified position

### Utility Operations
- `size()`: Get number of elements
- `isEmpty()`: Check if list is empty
- `clear()`: Remove all elements
- `toString()`: Get string representation

## Performance Characteristics

- Access by index: O(n/2) average case
- Insertion at ends: O(1)
- Insertion in middle: O(n)
- Deletion at ends: O(1)
- Deletion in middle: O(n)

## Testing

The project includes comprehensive tests that cover:
- Basic operations
- Edge cases
- Complex operations
- Performance optimizations

## Usage Example

```java
DoublyLinkedList<String> list = new DoublyLinkedList<>();

// Adding elements
list.addFirst("First");
list.addLast("Last");
list.add(1, "Middle");

// Accessing elements
String first = list.get(0);
String middle = list.get(1);
String last = list.get(2);

// Removing elements
String removed = list.remove(1);

// Checking size
int size = list.size();
```

## Best Practices Demonstrated

1. **Error Handling**
   - Proper exception handling
   - Input validation
   - Clear error messages

2. **Code Quality**
   - Comprehensive documentation
   - Clean code structure
   - Consistent naming conventions

3. **Testing**
   - Unit tests for all operations
   - Edge case coverage
   - Performance testing

## Future Improvements

Potential enhancements:
- Iterator implementation
- Reverse traversal
- Sorting capabilities
- Merge operations
- Circular list support 