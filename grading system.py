def get_grade(score):
    """Function to determine the grade based on the score."""
    if score >= 70 and score <= 100:
        return 'A'
    elif score >= 60 and score <= 69:
        return 'B'
    elif score >= 50 and score <= 59:
        return 'C'
    elif score >= 40 and score <= 49:
        return 'D'
    elif score < 39:
        return 'E (Fail)'
    else:
        return 'Invalid score'  

def main():
    # Prompt the user to enter their score
    try:
        score = float(input("Enter the student's score (0-100): "))
        if score < 0 or score > 100:
            print("Please enter a score between 0 and 100.")
        else:
            grade = get_grade(score)
            print(f"The student's grade is: {grade}")

            # Check if the student needs a supplementary examination
            if score < 40:
                print("The student is required to take a supplementary examination.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the score.")

if __name__ == "__main__":
    main()
