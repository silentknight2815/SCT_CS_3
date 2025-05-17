
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        'Length': not length_error,
        'Digits': not digit_error,
        'Uppercase': not uppercase_error,
        'Lowercase': not lowercase_error,
        'Symbols': not symbol_error,
    }

    strength = sum(errors.values())

    if strength == 5:
        verdict = "Very Strong 🔐"
    elif strength >= 3:
        verdict = "Moderate ⚠️"
    else:
        verdict = "Weak ❌"

    return errors, verdict

# Welcome Message
print("==========================================")
print("  Welcome to Password Strength Checker 🔐")
print("       Created by: Cyber Expert 💻🛡️")
print("==========================================\n")

# User input
password = input("Enter your password to check strength: ")

errors, verdict = check_password_strength(password)

print("\nPassword Strength Report:")
for key, passed in errors.items():
    symbol = "✅" if passed else "❌"
    print(f"{symbol} {key} check: {'Passed' if passed else 'Failed'}")

print(f"\nFinal Verdict: {verdict}") 



