import math

# Function to calculate the influencer score based on follower count and engagement percentage
def get_influencer_score(num_followers, average_engagement_percentage, base_multiplier=1):
    # Calculate the influencer score using logarithm base 2
    return base_multiplier * average_engagement_percentage * math.log(num_followers, 2)

# Main function to test the get_influencer_score function
def main():
    # Example 1
    num_followers = 1000
    average_engagement_percentage = 5  # Assuming 5% engagement
    base_multiplier = 2  # Base multiplier
    score = get_influencer_score(num_followers, average_engagement_percentage, base_multiplier)
    print(f"If the influencer has {num_followers} followers with {average_engagement_percentage}% engagement and a base multiplier of"
          f"{base_multiplier}, their influencer score is {score:.0f}.")

    # Example 2
    num_followers = 50000
    average_engagement_percentage = 10  # Assuming 10% engagement
    base_multiplier = 1.5  # Base multiplier
    score = get_influencer_score(num_followers, average_engagement_percentage, base_multiplier)
    print(f"If the influencer has {num_followers} followers with {average_engagement_percentage}% engagement and a base multiplier of"
          f"{base_multiplier}, their influencer score is {score:.0f}.")

    # Example 3
    num_followers = 1000000
    average_engagement_percentage = 2  # Assuming 2% engagement
    base_multiplier = 1  # Base multiplier
    score = get_influencer_score(num_followers, average_engagement_percentage, base_multiplier)
    print(f"If the influencer has {num_followers} followers with {average_engagement_percentage}% engagement and a base multiplier of"
          f"{base_multiplier}, their influencer score is {score:.0f}.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
