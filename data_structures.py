from collections import deque

# Demonstration of common Python data structures using a search algorithm

# Test case: Find if value 5 exists in the collection
test_data = [1, 3, 5, 7, 9]
search_value = 5

# 1. List
def search_list(data, value):
    return value in data

# 2. Tuple
def search_tuple(data, value):
    return value in data

# 3. Set
def search_set(data, value):
    return value in data

# 4. Dictionary (searching for value among keys)
def search_dict_keys(data, value):
    return value in data.keys()

# 5. Dictionary (searching for value among values)
def search_dict_values(data, value):
    return value in data.values()

# 6. Queue (using collections.deque)
def search_queue(data, value):
    return value in data

# 7. Stack (using list)
def search_stack(data, value):
    return value in data

# Prepare data structures
list_data = test_data
tuple_data = tuple(test_data)
set_data = set(test_data)
dict_data = {x: chr(65 + i) for i, x in enumerate(test_data)}
queue_data = deque(test_data)
stack_data = list(test_data)

# Run searches
print("List:", search_list(list_data, search_value))
print("Tuple:", search_tuple(tuple_data, search_value))
print("Set:", search_set(set_data, search_value))
print("Dict (keys):", search_dict_keys(dict_data, search_value))
print("Dict (values):", search_dict_values(dict_data, 'C'))  # Example: search for value 'C'
print("Queue:", search_queue(queue_data, search_value))
print("Stack:", search_stack(stack_data, search_value))