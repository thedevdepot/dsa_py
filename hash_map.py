# Problem: Given a list of integers, find if there are any two numbers that add up to a target value.
# We'll use a hash map to solve this efficiently, handling edge cases.

def two_sum(nums, target):
    # Edge case: nums is None or not a list
    if not isinstance(nums, list):
        return None
    # Edge case: nums has fewer than 2 elements
    if len(nums) < 2:
        return None

    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices of numbers that add up to target:", result)
# Output: Indices of numbers that add up to target: [0, 1]

# Edge case tests
print(two_sum([], 5))                # None (empty list)
print(two_sum([1], 1))               # None (only one element)
print(two_sum(None, 1))              # None (input is None)
print(two_sum([3, 3], 6))            # [0, 1] (duplicate numbers)
print(two_sum([1, 2, 3], 7))         # None (no solution)