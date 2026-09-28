/**
 * Bitwise and Logical Operations in C
 * 
 * This file demonstrates and explains all logical and bitwise operators available in C,
 * including their behavior, common use cases, and practical examples.
 * 
 * Logical Operators:
 * - AND (&&): Returns true only if both operands are true
 * - OR (||): Returns true if at least one operand is true
 * - NOT (!): Inverts the boolean value
 * 
 * Bitwise Operators:
 * - AND (&): Performs bitwise AND between each bit
 * - OR (|): Performs bitwise OR between each bit
 * - XOR (^): Performs bitwise XOR between each bit
 * - NOT (~): Inverts all bits
 * - Left Shift (<<): Shifts bits to the left
 * - Right Shift (>>): Shifts bits to the right
 * 
 * Additional Operations:
 * - NAND: Combination of AND and NOT
 * - NOR: Combination of OR and NOT
 * - XNOR: Combination of XOR and NOT
 */

#include <stdio.h>
#include <stdbool.h>

/**
 * Demonstrates basic logical operators (&&, ||, !)
 * 
 * Logical operators work with boolean values (true/false) and
 * are commonly used in conditional statements and loops.
 */
void demonstrateLogicalOperators() {
    printf("\n=== Logical Operators ===\n");
    
    bool a = true;
    bool b = false;
    
    printf("a = %d, b = %d\n", a, b);
    printf("a && b = %d (Logical AND)\n", a && b);
    printf("a || b = %d (Logical OR)\n", a || b);
    printf("!a = %d (Logical NOT)\n", !a);
    printf("!b = %d (Logical NOT)\n", !b);
}

/**
 * Demonstrates basic bitwise operators (&, |, ^, ~)
 * 
 * Bitwise operators work directly on the binary representation
 * of numbers, manipulating individual bits.
 */
void demonstrateBitwiseOperators() {
    printf("\n=== Bitwise Operators ===\n");
    
    unsigned char a = 0xAA;  // Binary 10101010, 170 in decimal
    unsigned char b = 0xF0;  // Binary 11110000, 240 in decimal
    
    printf("a = %d (binary: 10101010)\n", a);
    printf("b = %d (binary: 11110000)\n", b);
    printf("a & b = %d (Bitwise AND)\n", a & b);
    printf("a | b = %d (Bitwise OR)\n", a | b);
    printf("a ^ b = %d (Bitwise XOR)\n", a ^ b);
    printf("~a = %d (Bitwise NOT)\n", (unsigned char)~a);
}

/**
 * Demonstrates bit shifting operations (<<, >>)
 * 
 * Shift operators move all bits in a number left or right by
 * a specified number of positions. This is equivalent to
 * multiplying or dividing by powers of 2.
 */
void demonstrateShiftOperators() {
    printf("\n=== Shift Operators ===\n");
    
    unsigned char num = 0x0A;  // Binary 00001010, 10 in decimal
    
    printf("Original number: %d (binary: 00001010)\n", num);
    printf("Left shift by 2: %d (binary: 00101000)\n", num << 2);
    printf("Right shift by 1: %d (binary: 00000101)\n", num >> 1);
}

/**
 * Demonstrates compound bitwise operations (NAND, NOR, XNOR)
 * 
 * These operations are combinations of basic bitwise operators
 * and are useful in digital logic and circuit design.
 */
void demonstrateCompoundOperations() {
    printf("\n=== Compound Bitwise Operations ===\n");
    
    unsigned char a = 0xAA;
    unsigned char b = 0xF0;
    
    // NAND: NOT (A AND B)
    unsigned char nand = ~(a & b);
    printf("NAND: %d (NOT of A AND B)\n", nand);
    
    // NOR: NOT (A OR B)
    unsigned char nor = ~(a | b);
    printf("NOR: %d (NOT of A OR B)\n", nor);
    
    // XNOR: NOT (A XOR B)
    unsigned char xnor = ~(a ^ b);
    printf("XNOR: %d (NOT of A XOR B)\n", xnor);
}

/**
 * Demonstrates practical applications of bitwise operations
 * 
 * These examples show common use cases for bitwise operations
 * in real-world programming scenarios.
 */
void demonstratePracticalApplications() {
    printf("\n=== Practical Applications ===\n");
    
    // 1. Checking if a number is even or odd
    int num = 42;
    printf("Number %d is %s\n", num, (num & 1) ? "odd" : "even");
    
    // 2. Setting a specific bit
    unsigned char flags = 0;
    unsigned char bit_to_set = 3;  // Set the 4th bit
    flags |= (1 << bit_to_set);
    printf("After setting bit %d: %d\n", bit_to_set, flags);
    
    // 3. Clearing a specific bit
    flags &= ~(1 << bit_to_set);
    printf("After clearing bit %d: %d\n", bit_to_set, flags);
    
    // 4. Toggling a specific bit
    flags ^= (1 << bit_to_set);
    printf("After toggling bit %d: %d\n", bit_to_set, flags);
    
    // 5. Checking if a bit is set
    printf("Bit %d is %s\n", bit_to_set, 
           (flags & (1 << bit_to_set)) ? "set" : "not set");
}

/**
 * Demonstrates comparison operators and their bitwise equivalents
 * 
 * Comparison operators return boolean values, while their bitwise
 * equivalents can be used for more complex operations.
 */
void demonstrateComparisonOperators() {
    printf("\n=== Comparison Operators ===\n");
    
    int a = 5;
    int b = 3;
    
    printf("a = %d, b = %d\n", a, b);
    printf("a == b: %d (Equal to)\n", a == b);
    printf("a != b: %d (Not equal to)\n", a != b);
    printf("a > b: %d (Greater than)\n", a > b);
    printf("a < b: %d (Less than)\n", a < b);
    printf("a >= b: %d (Greater than or equal to)\n", a >= b);
    printf("a <= b: %d (Less than or equal to)\n", a <= b);
    
    // Bitwise comparison examples
    printf("\nBitwise Comparison Examples:\n");
    printf("a & b == 0: %d (Check if no common bits)\n", (a & b) == 0);
    printf("a | b == a + b: %d (Check if no overlapping bits)\n", (a | b) == (a + b));
}

/**
 * Demonstrates compound assignment operators
 * 
 * These operators combine an operation with assignment,
 * making the code more concise and often more efficient.
 */
void demonstrateCompoundAssignment() {
    printf("\n=== Compound Assignment Operators ===\n");
    
    int a = 5;
    int b = 3;
    
    printf("Initial values: a = %d, b = %d\n", a, b);
    
    a &= b;  // a = a & b
    printf("After a &= b: a = %d\n", a);
    
    a |= b;  // a = a | b
    printf("After a |= b: a = %d\n", a);
    
    a ^= b;  // a = a ^ b
    printf("After a ^= b: a = %d\n", a);
    
    a <<= 2;  // a = a << 2
    printf("After a <<= 2: a = %d\n", a);
    
    a >>= 1;  // a = a >> 1
    printf("After a >>= 1: a = %d\n", a);
}

/**
 * Demonstrates bit manipulation techniques
 * 
 * These are common techniques used in low-level programming
 * and system development.
 */
void demonstrateBitManipulation() {
    printf("\n=== Bit Manipulation Techniques ===\n");
    
    unsigned int num = 0xAA;
    
    // 1. Isolating the rightmost set bit
    unsigned int rightmost = num & (-num);
    printf("Rightmost set bit: %d\n", rightmost);
    
    // 2. Clearing the rightmost set bit
    unsigned int cleared = num & (num - 1);
    printf("After clearing rightmost set bit: %d\n", cleared);
    
    // 3. Getting the position of the rightmost set bit
    int position = 0;
    unsigned int temp = num;
    while ((temp & 1) == 0) {
        temp >>= 1;
        position++;
    }
    printf("Position of rightmost set bit: %d\n", position);
    
    // 4. Checking if a number is a power of 2
    bool isPowerOf2 = (num & (num - 1)) == 0;
    printf("Is power of 2: %d\n", isPowerOf2);
    
    // 5. Counting set bits
    int count = 0;
    temp = num;
    while (temp) {
        count += temp & 1;
        temp >>= 1;
    }
    printf("Number of set bits: %d\n", count);
}

/**
 * Demonstrates advanced bitwise operations
 * 
 * These operations are useful in specific scenarios like
 * cryptography, compression, and low-level system programming.
 */
void demonstrateAdvancedOperations() {
    printf("\n=== Advanced Bitwise Operations ===\n");
    
    unsigned int a = 0xAA;
    unsigned int b = 0xF0;
    
    // 1. Bit rotation
    unsigned int rotated = (a << 1) | (a >> 7);  // Rotate left by 1
    printf("Rotated left by 1: %d\n", rotated);
    
    // 2. Bit reversal
    unsigned int reversed = 0;
    for (int i = 0; i < 8; i++) {
        reversed = (reversed << 1) | (a & 1);
        a >>= 1;
    }
    printf("Bit reversed: %d\n", reversed);
    
    // 3. Parity check
    unsigned int parity = 0;
    a = 0xAA;
    while (a) {
        parity ^= a & 1;
        a >>= 1;
    }
    printf("Parity: %d\n", parity);
    
    // 4. Absolute value without branching
    int value = -42;
    int mask = value >> 31;
    int abs_value = (value + mask) ^ mask;
    printf("Absolute value of %d: %d\n", value, abs_value);
    
    // 5. Swap without temporary variable
    a = 5;
    b = 3;
    printf("Before swap: a = %d, b = %d\n", a, b);
    a ^= b;
    b ^= a;
    a ^= b;
    printf("After swap: a = %d, b = %d\n", a, b);
}

/**
 * Main function demonstrating all bitwise and logical operations
 * 
 * This function serves as an entry point and demonstrates all
 * the different types of operations available in C.
 */
int main() {
    printf("Bitwise and Logical Operations in C\n");
    printf("==================================\n");
    
    demonstrateLogicalOperators();
    demonstrateBitwiseOperators();
    demonstrateShiftOperators();
    demonstrateCompoundOperations();
    demonstratePracticalApplications();
    demonstrateComparisonOperators();
    demonstrateCompoundAssignment();
    demonstrateBitManipulation();
    demonstrateAdvancedOperations();
    
    return 0;
}
