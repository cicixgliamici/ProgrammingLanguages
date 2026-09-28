#include <assert.h>

/* The Exercism implementation is small enough to test as one translation unit. */
#include "../Exercism/0001- Gregorian-calendar.c"

static void test_century_rules(void) {
    assert(leap_year(2000));
    assert(!leap_year(1900));
}

static void test_regular_year_rules(void) {
    assert(leap_year(2024));
    assert(!leap_year(2023));
}

int main(void) {
    test_century_rules();
    test_regular_year_rules();
    return 0;
}
