#include <assert.h>
#include <stddef.h>

/*
 * The lesson is intentionally a self-contained executable. Renaming its entry
 * point lets this focused test reuse the demonstrated implementation without
 * hiding it behind a second copy.
 */
#define main binary_search_lesson_main
#include "../06_binary_search.c"
#undef main

static void test_iterative_search(void) {
    const int values[] = {-8, -1, 0, 4, 9, 17};
    const int length = (int)(sizeof(values) / sizeof(values[0]));

    assert(binarySearchIterative(values, length, -8) == 0);
    assert(binarySearchIterative(values, length, 17) == length - 1);
    assert(binarySearchIterative(values, length, 4) == 3);
    assert(binarySearchIterative(values, length, 3) == -1);
}

static void test_recursive_search(void) {
    const int values[] = {2, 5, 8, 12, 16};
    const int length = (int)(sizeof(values) / sizeof(values[0]));

    assert(binarySearchRecursive(values, 0, length - 1, 8) == 2);
    assert(binarySearchRecursive(values, 0, length - 1, 7) == -1);
    assert(binarySearchRecursive(values, 0, -1, 7) == -1);
}

static void test_empty_input(void) {
    assert(binarySearchIterative(NULL, 0, 10) == -1);
    assert(binarySearchRecursive(NULL, 0, -1, 10) == -1);
}

int main(void) {
    test_iterative_search();
    test_recursive_search();
    test_empty_input();
    return 0;
}
