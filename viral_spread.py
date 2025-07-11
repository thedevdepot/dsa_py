#!/usr/bin/env python3
"""
This script shows how a post that goes viral spreads according to x**1.2
"""

# Define a list of followers count as a list of followers with the amount they have as followers
followers_count = [2, 20, 10, 25]

# Function to calculate the viral spread
def calculate_viral_spread(follower_counts): #notice follwer_counts is a different variable than followers_count
    # Check if the list of follower counts is empty
    if not follower_counts:
        # If the list is empty, return 0
        return 0
    
    # Initialize a list to store the viral spread for each follower count
    viral_spreads = []
    
    # Loop through each follower count
    for count in follower_counts:
        # Calculate the viral spread for this follower count according to x**1.2
        viral_spread = count ** 1.2
        # Append the viral spread to the list
        viral_spreads.append(viral_spread)
    
    # Calculate the total viral spread by summing up all the individual spreads
    total_viral_spread = sum(viral_spreads)
    
    # Return the total viral spread
    return total_viral_spread

# Main function
def main():
    # Calculate the viral spread for the given follower counts
    new_followers = calculate_viral_spread(followers_count)
    
    # Print the result
    print(f"If the initial followers had their own followers with counts {followers_count} then your new follower count is {int(new_followers)}.")

# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    # Call the main function
    main()
