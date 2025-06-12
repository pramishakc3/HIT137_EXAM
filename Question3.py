# question3.py
# HIT137 - Final Exam 2025 S1
# Author: [Your Name]
# This script prints a symmetric star pattern using both a loop-based and a recursive approach,
# and compares their execution times.

import time

def print_pattern_with_for():
    """
    Prints the required symmetric star pattern using for-loops.
    The pattern has an upper half and a lower half, both symmetric.
    """
    lines = 5  # Number of lines in the upper half (excluding the center line)

    # Print top part of the pattern
    for row in range(1, lines + 1):
        left_stars = '*' * row
        spaces = ' ' * (2 * (lines - row))
        right_stars = '*' * row
        print(left_stars + spaces + right_stars)

    # Print bottom part of the pattern
    for row in range(lines - 1, 0, -1):
        left_stars = '*' * row
        spaces = ' ' * (2 * (lines - row))
        right_stars = '*' * row
        print(left_stars + spaces + right_stars)

def print_pattern_top_recursive(current, total):
    """
    Recursively prints the upper half of the pattern.
    :param current: Current row number (starts at 1)
    :param total: Total number of lines in the upper half
    """
    if current > total:
        return
    left_stars = '*' * current
    spaces = ' ' * (2 * (total - current))
    right_stars = '*' * current
    print(left_stars + spaces + right_stars)
    print_pattern_top_recursive(current + 1, total)

def print_pattern_bottom_recursive(current, total):
    """
    Recursively prints the lower half of the pattern.
    :param current: Current row number (starts at total-1, decreases to 1)
    :param total: Total number of lines in the upper half
    """
    if current == 0:
        return
    left_stars = '*' * current
    spaces = ' ' * (2 * (total - current))
    right_stars = '*' * current
    print(left_stars + spaces + right_stars)
    print_pattern_bottom_recursive(current - 1, total)

def print_pattern_with_recursion():
    """
    Prints the required symmetric star pattern using recursion.
    """
    lines = 5
    print_pattern_top_recursive(1, lines)
    print_pattern_bottom_recursive(lines - 1, lines)

def main():
    # Print and time the loop-based pattern
    print("Pattern using for-loops:\n")
    start_loop = time.time()
    print_pattern_with_for()
    end_loop = time.time()
    loop_time = end_loop - start_loop

    # Print and time the recursive pattern
    print("\nPattern using recursion:\n")
    start_rec = time.time()
    print_pattern_with_recursion()
    end_rec = time.time()
    rec_time = end_rec - start_rec

    # Show timing results
    print("\nTime taken for execution (Loop): {:.6f} seconds".format(loop_time))
    print("Time taken for execution (Recursion): {:.6f} seconds".format(rec_time))

if __name__ == "__main__":
    main()