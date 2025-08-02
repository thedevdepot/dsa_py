# Here’s a classic LeetCode example for finding the missing number in an array containing
# n distinct numbers taken from 0 to n. One number is missing.

def find_missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)

# Example:
nums1 = [3, 0, 1]
print(find_missing_number(nums1))  # Output: 2

# Edge Cases:
# 1. Missing number is 0
nums2 = [1, 2, 3]
print(find_missing_number(nums2))  # Output: 0

# 2. Missing number is n
nums3 = [0, 1, 2]
print(find_missing_number(nums3))  # Output: 3

# 3. Array has only one element
nums4 = [0]
print(find_missing_number(nums4))  # Output: 1

# 4. Array is empty
nums5 = []
print(find_missing_number(nums5))  # Output: 0