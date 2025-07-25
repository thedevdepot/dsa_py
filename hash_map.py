# Problem: Given a list of integers, find if there are any two numbers that add up to a target value.
# We'll use a hash map to solve this efficiently.

def two_sum(nums, target):
    # Create an empty hash map to store numbers we've seen so far
    num_map = {}
    # Iterate through the list with index and value
    for i, num in enumerate(nums):
        # Calculate the complement that would sum to the target
        complement = target - num
        # Check if the complement is already in the hash map
        if complement in num_map:
            # If found, return the indices of the two numbers
            return [num_map[complement], i]
        # Otherwise, store the current number and its index in the hash map
        num_map[num] = i
    # If no pair is found, return None
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices of numbers that add up to target:", result)
# Output: Indices of numbers that add up to target: [0, 1]