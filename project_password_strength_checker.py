import string

# ==========================================================
#               PASSWORD STRENGTH CHECKER
# ==========================================================

def check_password_strength(password: str):
    score = 0
    criteria_met = 0

    # Check required character categories
    if any(char.isupper() for char in password):
        score += 1
        criteria_met += 1

    if any(char.islower() for char in password):
        score += 1
        criteria_met += 1

    if any(char.isdigit() for char in password):
        score += 1
        criteria_met += 1

    if any(char in string.punctuation for char in password):
        score += 1
        criteria_met += 1

    # If all conditions are not satisfied, return current score
    if criteria_met < 4:
        return score, criteria_met

    # Additional score based on password length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if len(password) >= 20:
        score += 1

    return score, criteria_met


def check_password(password: str) -> None:

    # Load commonly used passwords
    with open("co_hussain_shoaib.txt", "r") as file:
        common_passwords = set(file.read().splitlines())

    # Check if password is too common
    if password in common_passwords:
        print("\nPassword is too common.")
        print("Password Strength: 0/8\n")
        return

    # Evaluate password strength
    score, criteria_met = check_password_strength(password)

    print("\nPassword Strength Score:", score)

    if score == 0:
        print("Password is extremely weak.")

    elif score == 1:
        print("Password is weak.")

    elif score == 2:
        print("Password strength is average.")

    elif score == 3 or score == 4:
        print("Password is moderately strong.")

    else:
        print("Password is extremely strong.")

    # Missing requirements warning
    if criteria_met < 4:
        print("\nPassword must include:")
        print("- At least one uppercase letter")
        print("- At least one lowercase letter")
        print("- At least one digit")
        print("- At least one special character")

    print()


# ==========================================================
#                 PROJECT TITLE PAGE
# ==========================================================

print("\n")
print("=" * 70)
print(" " * 22 + "PIEAS")
print(" " * 10 + "Department of Physics and Applied Mathematics")
print("=" * 70)

print("\n")
print(" " * 20 + "PROJECT SUBMISSION")
print("\n")

print("*" * 70)
print(" " * 18 + "PASSWORD STRENGTH CHECKER")
print("*" * 70)

print("\n")
print("Course Name : AICT")
print("Instructor  : Atif Raza")

print("\n")
print("-" * 70)
print("Submission Date : May 4, 2026")
print("-" * 70)

print("Submitted By:")
print("1. Hussain Ahmed")
print("2. Muhammad Shoaib")

print("\n")
print("=" * 70)
print(" " * 22 + "SESSION 2025 - 2029")
print("=" * 70)

print("\nThank You!\n")


# ==========================================================
#                    MAIN PROGRAM LOOP
# ==========================================================

while True:
    password = input("Enter Password: ")
    check_password(password)