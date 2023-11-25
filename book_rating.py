# Function to get a rating from the user within the specified range (0-5)
def get_rating(category):
    while True:
        
        # Not all criteria are always applicable so users can opt out of them
        # by entering 0
        rating = input(f"Rate {category} (0-5, enter 0 if not applicable): ")
        if rating.isdigit() and 0 <= int(rating) <= 5:
            return int(rating)

# Function to round a rating to the nearest integer, considering decimal part
def round_rating(rating):
    decimal_part = rating % 1

    # If the decimal part is 0.5, ask the user for a more detailed impression
    # to decide to round up or down
    if decimal_part == 0.5:
        impression = input("Was your overall impression more positive (p) "
                           "or negative (n)? ")
        return int(rating + 0.5) if impression.lower() == 'p' else int(rating)
    else:
        return int(rating + 0.5) if decimal_part >= 0.5 else int(rating)

# Main function to gather ratings based on user input    
def main():
    
    # The rating criteria would be different for fiction and non-fiction
    genre = input("Enter 'f' for fiction or 'n' for non-fiction: ")

    if genre == 'f':
        plot = get_rating("Plot and Storyline \n- 1: Weak, lacks coherence and "
                          "originality.\n- 5: Strong, well-developed, and "
                          "original plot with unexpected twists.")
        characterization = get_rating("Characterization\n- 1: Superficial "
                                      "characters with little depth or "
                                      "development. \n- 5: Complex, authentic "
                                      "characters with significant growth and "
                                      "evolution.")
        writing_style = get_rating("Writing Style\n- 1: Poorly crafted prose, "
                                   "difficult to follow.\n- 5: Engaging "
                                   "writing style, rich language, and "
                                   "effective pacing.")
        themes_messages = get_rating("Themes and Messages\n- 1: Unclear or "
                                     "superficial themes.\n- 5: Profound and "
                                     "thought-provoking themes that resonate.")
        impact_enjoyment = get_rating("Impact and Enjoyment\n- 1: Fails to "
                                      "engage or leaves a negative impression."
                                      "\n- 5: Highly impactful, enjoyable, and "
                                      "memorable.")

    elif genre == 'n':
        accuracy_reliability = get_rating("Accuracy and Reliability"
                                          "\n- 1: Inaccurate information, "
                                          "unreliable sources."
                                          "\n- 5: Highly accurate, "
                                          "well-researched content from "
                                          "credible sources.")
        clarity_accessibility = get_rating("Clarity and Accessibility"
                                           "\n- 1: Confusing, difficult to "
                                           "understand.\n- 5: Clear, "
                                           "accessible language for a wide "
                                           "audience.")
        depth_research = get_rating("Depth of Research\n- 1: Superficial "
                                    "research, lacking depth. \n- 5: Thorough "
                                    "research, extensive use of credible "
                                    "sources.")
        relevance_timeliness = get_rating("Relevance and Timeliness"
                                          "\n- 1: Outdated or irrelevant "
                                          "information.\n- 5: Timely, "
                                          "relevant, and applicable to current "
                                          "contexts.")
        author_perspective_bias = get_rating("Author's Perspective and Bias"
                                             "\n- 1: Strong, unacknowledged "
                                             "bias affecting the objectivity."
                                             "\n- 5: Transparent perspective, "
                                             "minimal bias, and balanced "
                                             "presentation.")

    # Combine the ratings based on genre
    ratings = [plot, characterization, writing_style, themes_messages, 
               impact_enjoyment] if genre == 'f' else [accuracy_reliability,
                                                       clarity_accessibility, 
                                                       depth_research, 
                                                       relevance_timeliness, 
                                                       author_perspective_bias]

    # Filter out zero (non-applicable) ratings
    non_zero_ratings = [rating for rating in ratings if rating != 0]

    if non_zero_ratings:
        # Calculate and display the overall rating
        average_rating = round_rating(sum(non_zero_ratings) 
                                      / len(non_zero_ratings))
        print(f"\nOverall rating: {average_rating}")

# Entry point of the program
if __name__ == "__main__":
    main()
                                                                                