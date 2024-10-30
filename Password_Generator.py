import random
import string
import secrets

def generate_password(length=16):
    """
    Generates a strong password of the specified length.

    Args:
        length (int): The length of the password. Defaults to 16.

    Returns:
        str: A strong password of the specified length.

    Raises:
        ValueError: If the password length is less than 12.
    """
    if length < 12:
        raise ValueError("Password length should be at least 12 characters for enhanced security.")

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Combine all character sets
    all_chars = lower + upper + digits + special

    # Ensure password meets complexity requirements
    while True:
        password = ''.join(secrets.choice(all_chars) for _ in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
            and sum(c in special for c in password) >= 2):
            return password

def main():
    try:
        password_length = int(input("Enter desired password length (at least 12): "))
        strong_password = generate_password(password_length)
        print(f"Your generated password is: {strong_password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
