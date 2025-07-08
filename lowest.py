#!/usr/bin/env python3
"""
Find Minimum Value in a List
============================
This script defines a function to find the minimum value in a list of numbers.
"""

def find_minimum(nums):
    """
    Find the minimum value in a list of numbers.

    Args:
        nums (list): A list of numbers.

    Returns:
        The minimum value in the list, or None if the list is empty.
    """
    if len(nums) == 0:
        return None
    min_val = float("inf")
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val

def main():
    # Test the function
    numbers = [5, 2, 9, 1, 7]
    print("Minimum value:", find_minimum(numbers))

    # Test edge case: empty list
    print("Minimum value of empty list:", find_minimum([]))

if __name__ == "__main__":
    main()
