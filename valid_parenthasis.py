# Efficient version: O(n) time, O(n) space
def is_valid_parenthesis(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

# Explanatory version: step-by-step comments
def is_valid_parenthesis_explained(s: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    # Dictionary to match closing to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty or top doesn't match, invalid
            if not stack or stack[-1] != mapping[char]:
                return False
            # Pop the matched opening bracket
            stack.pop()
        # Ignore other characters (optional)
    # If stack is empty, all brackets matched
    return len(stack) == 0

# Example usage and edge cases
test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("", True),           # Edge case: empty string
    ("(", False),         # Edge case: single opening
    (")", False),         # Edge case: single closing
    ("((()))", True),     # Nested valid
    ("((())", False),     # Nested invalid
    ("abc", True),        # No brackets
]

for s, expected in test_cases:
    result = is_valid_parenthesis(s)
    print(f"is_valid_parenthesis({s!r}) = {result} (expected: {expected})")