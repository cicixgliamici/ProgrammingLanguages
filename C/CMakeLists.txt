cmake_minimum_required(VERSION 3.20)

project(c_learning_examples LANGUAGES C)

include(CTest)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

# Each lesson owns a main function, so every source must be a separate target.
set(LESSON_SOURCES
    00_helloWorld.c
    01_bitwise_operations.c
    02_list.c
    03_memory_management_intro.c
    04_queue.c
    05_stack.c
    06_binary_search.c
    07_binary_search_tree.c
)

foreach(lesson_source IN LISTS LESSON_SOURCES)
    get_filename_component(lesson_name "${lesson_source}" NAME_WE)
    add_executable("${lesson_name}" "${lesson_source}")

    # Warnings expose mistakes while keeping the examples portable across compilers.
    if(MSVC)
        target_compile_options("${lesson_name}" PRIVATE /W4)
    else()
        target_compile_options("${lesson_name}" PRIVATE -Wall -Wextra -Wpedantic)
    endif()

    # Running each lesson catches crashes in addition to compilation errors.
    add_test(NAME "run_${lesson_name}" COMMAND "${lesson_name}")
endforeach()
