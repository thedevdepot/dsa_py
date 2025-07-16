# Function to find last name by iterating over dictionary items
def find_last_name(names_dict, first_name):
    # Iterate over all items in the dictionary
    for current_first_name, last_name in names_dict.items():
        if current_first_name == first_name:
            return last_name
    # Return None if first name not found
    return None

# Function to find last name using dictionary lookup
def find_last_name_constant(names_dict, first_name):
    # Directly get the last name from the dictionary
    return names_dict.get(first_name)

# Test examples
names_dict = {
    "John": "Doe",
    "Jane": "Doe",
    "Alice": "Smith",
    "Bob": "Johnson",
    "Eve": "Williams"
}

# Test cases
test_cases = [
    {"first_name": "John", "description": "Find existing name"},
    {"first_name": "Alice", "description": "Find existing name"},
    {"first_name": "Mike", "description": "Find non-existing name"}
]

# Run test cases for both functions
for test_case in test_cases:
    print(f"\nTest case: {test_case['description']} - {test_case['first_name']}")

    # Run original function
    print("Original function (O(n)):")
    last_name = find_last_name(names_dict, test_case['first_name'])
    print(f"Last name for {test_case['first_name']}: {last_name}")

    # Run constant time function
    print("Constant time function (O(1)):")
    last_name = find_last_name_constant(names_dict, test_case['first_name'])
    print(f"Last name for {test_case['first_name']}: {last_name}")
