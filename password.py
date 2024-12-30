import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on specific criteria.

    Criteria:
    - Minimum length of 8 characters.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one number.
    - Contains at least one special character (!@#$%^&*()-_=+[{]}\\|;:'",<.>/?).

    Returns:
    - A dictionary with the assessment details and an overall strength rating.
    """
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "number": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*()\-_=+\[{\]}\\|;:'\",<.>/?]", password)),
    }

    score = sum(criteria.values())
    strength = "Weak"
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"

    return {
        "criteria": criteria,
        "score": score,
        "strength": strength,
    }


if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    result = assess_password_strength(password)
    print("\nPassword Strength Assessment:")
    for criterion, met in result["criteria"].items():
        print(f"- {criterion.capitalize()}: {'Met' if met else 'Not Met'}")
    print(f"\nOverall Strength: {result['strength']}")
