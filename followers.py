# Define a function to predict the follower count of an influencer after a certain number of months.
# The prediction is based on the current follower count, the type of influencer, and the number of months.
def get_follower_prediction(follower_count, follower_type, num_months):
    """
    Predicts the follower count of an influencer after a certain number of months.

    Args:
        follower_count (int): The current follower count of the influencer.
        follower_type (str): The type of influencer (e.g., "fitness", "cosmetic").
        num_months (int): The number of months to predict the follower count for.

    Returns:
        int: The predicted follower count after the specified number of months.
    """
    # Initialize a factor variable to store the growth rate multiplier for the influencer type.
    # This factor will be used to calculate the predicted follower count.
    factor = 2
    
    # Use a match statement to determine the growth rate factor based on the influencer type.
    # This allows for easy addition of more influencer types in the future.
    match follower_type:
        case "fitness":
            # Fitness influencers have a higher growth rate factor of 4.
            factor = 4
        case "cosmetic":
            # Cosmetic influencers have a growth rate factor of 3.
            factor = 3
    
    # Calculate the predicted follower count by multiplying the current follower count with the growth rate factor and the number of months.
    # This assumes a linear growth model where the follower count increases by a fixed amount each month.
    return follower_count * (factor * num_months)


# Define a main function to test the get_follower_prediction function with different scenarios.
def main():
    # Test scenario 1: Fitness influencer with 1000 followers for 6 months.
    follower_count = 1000
    follower_type = "fitness"
    num_months = 6
    predicted_followers = get_follower_prediction(follower_count, follower_type, num_months)
    print(f"Test Scenario 1: Fitness influencer with {follower_count} followers for {num_months} months.")
    print(f"Predicted followers: {predicted_followers}")
    print()

    # Test scenario 2: Cosmetic influencer with 500 followers for 3 months.
    follower_count = 500
    follower_type = "cosmetic"
    num_months = 3
    predicted_followers = get_follower_prediction(follower_count, follower_type, num_months)
    print(f"Test Scenario 2: Cosmetic influencer with {follower_count} followers for {num_months} months.")
    print(f"Predicted followers: {predicted_followers}")
    print()

    # Test scenario 3: Default growth rate for an influencer with 2000 followers for 9 months.
    follower_count = 2000
    follower_type = "tech"
    num_months = 9
    predicted_followers = get_follower_prediction(follower_count, follower_type, num_months)
    print(f"Test Scenario 3: Default growth rate for an influencer with {follower_count} followers for {num_months} months.")
    print(f"Predicted followers: {predicted_followers}")


# Call the main function to run the test scenarios.
if __name__ == "__main__":
    main()  
