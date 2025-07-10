# Define a function to calculate the sum of a list of numbers
def calculate_sum(nums):
    """
    Calculate the sum of a list of numbers.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of the numbers in the list.
    """
    # Initialize a variable to store the sum
    s = 0
    # Iterate over each number in the list
    for n in nums:
        # Add the number to the sum
        s += n
    # Return the final sum
    return s

# Define a main function to handle user input and output
def main():
    # Define a default list of numbers
    default_nums = [1, 5, 7, 9]

    # Prompt the user to enter numbers separated by spaces
    user_input = input("Enter numbers separated by spaces (or press Enter to use the default list): ")

    # Check if the user wants to use the default list
    if user_input.strip() == "":
        # Use the default list
        nums = default_nums
        print("Using default list:", nums)
    else:
        # Try to convert the user's input to a list of integers
        try:
            # Split the input string into individual numbers and convert to integers
            nums = [int(x) for x in user_input.split()]
        except ValueError:
            # If the input is invalid, use the default list and print an error message
            print("Invalid input. Using default list.")
            nums = default_nums

    # Calculate the sum of the numbers
    result = calculate_sum(nums)

    # Print the result
    print(f"The sum of the list {nums} is: {result}")

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function
    main()
