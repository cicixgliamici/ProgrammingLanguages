/* 
 * This is a simple C program that prints "Hello, World!" to the console.
 * It demonstrates the basic structure of a C program with detailed comments.
 */

/* 
 * The following preprocessor directive includes the Standard Input Output library.
 * This library contains the declarations for input/output functions such as printf.
 */
#include <stdio.h>

/*
 * The main() function is the entry point of every C program.
 * When the program starts, execution begins here.
 */
int main() {

    /*
     * The printf function prints formatted output to the console.
     * Here, it is used to display the text "Hello, World!".
     * The "\n" at the end of the string is an escape sequence that moves the cursor to a new line.
     */
    printf("Hello, World!\n");

    /*
     * The return statement ends the main() function and returns a value to the operating system.
     * A return value of 0 typically signifies that the program executed successfully.
     */
    return 0;
}
