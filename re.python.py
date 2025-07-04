import re

def assess_password_strength(password):
    """
    Assesses the strength of a given password based on multiple criteria.

    Criteria include:
    - Length
    - Presence of uppercase letters
    - Presence of lowercase letters
    - Presence of numbers
    - Presence of special characters

    Args:
        password (str): The password string to assess.

    Returns:
        dict: A dictionary containing the strength score and feedback messages.
    """
    strength_score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 12:
        strength_score += 2
        feedback.append("Excellent length: Your password is 12 characters or more.")
    elif len(password) >= 8:
        strength_score += 1
        feedback.append("Good length: Your password is 8 characters or more.")
    else:
        feedback.append("Weak length: Consider making your password longer (at least 8 characters).")

    # 2. Uppercase Letter Check
    if re.search(r"[A-Z]", password):
        strength_score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Missing uppercase letters: Add at least one uppercase letter.")

    # 3. Lowercase Letter Check
    if re.search(r"[a-z]", password):
        strength_score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Missing lowercase letters: Add at least one lowercase letter.")

    # 4. Number Check
    if re.search(r"\d", password):
        strength_score += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("Missing numbers: Add at least one number.")

    # 5. Special Character Check (using a common set of special characters)
    special_characters = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?`~]"
    if re.search(special_characters, password):
        strength_score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("Missing special characters: Add at least one special character (e.g., !, @, #, $).")

    # Determine overall strength based on score
    overall_strength = ""
    if strength_score >= 6:
        overall_strength = "Very Strong"
    elif strength_score >= 4:
        overall_strength = "Strong"
    elif strength_score >= 2:
        overall_strength = "Moderate"
    else:
        overall_strength = "Weak"

    feedback.insert(0, f"Overall Strength: {overall_strength}")

    return {
        "score": strength_score,
        "overall_strength": overall_strength,
        "feedback": feedback
    }

if __name__ == "__main__":
    print("--- Password Strength Assessor ---")
    while True:
        user_password = input("Enter your password (or 'quit' to exit): ")
        if user_password.lower() == 'quit':
            break

        assessment_result = assess_password_strength(user_password)

        print("\n--- Assessment Results ---")
        for message in assessment_result["feedback"]:
            print(f"- {message}")
        print(f"Your password scored: {assessment_result['score']}/6 points.")
        print("--------------------------\n")

    print("Thank you for using the password strength assessor!")
