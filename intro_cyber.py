# intro_cyber.py

# Demonstrating different data structures in Python

# 1. List: Ordered, mutable, allows duplicates
fruits = ['apple', 'banana', 'cherry']
print("List:", fruits)

# 2. Tuple: Ordered, immutable, allows duplicates
coordinates = (10.0, 20.0)
print("Tuple:", coordinates)

# 3. Set: Unordered, mutable, no duplicates
unique_numbers = {1, 2, 3, 2, 1}
print("Set:", unique_numbers)

# 4. Dictionary: Key-value pairs, unordered (Python 3.7+ preserves insertion order)
person = {'name': 'Alice', 'age': 30}
print("Dictionary:", person)

# 5. String: Immutable sequence of characters
greeting = "Hello, World!"
print("String:", greeting)

# 6. Range: Immutable sequence of numbers
numbers = range(5)
print("Range:", list(numbers))

# 7. Bytearray: Mutable sequence of bytes
data = bytearray([65, 66, 67])
print("Bytearray:", data)

# 8. Frozenset: Immutable set
frozen = frozenset([1, 2, 3])
print("Frozenset:", frozen)
