import random
import string
import secrets

def generate_password(length=8):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    all_chars = lower + upper + digits + special
    
    while True:
        password = ''.join(secrets.choice(all_chars) for _ in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 2
            and sum(c in special for c in password) >= 1):
            return password

def strengthen_password(base_password):
    if len(base_password) < 8:
        raise ValueError("Base password should be at least 8 characters long.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = list(base_password)
    
    if not any(c.islower() for c in password):
        password.append(secrets.choice(lower))
    if not any(c.isupper() for c in password):
        password.append(secrets.choice(upper))
    if sum(c.isdigit() for c in password) < 2:
        password.extend(secrets.choice(digits) for _ in range(2 - sum(c.isdigit() for c in password)))
    if sum(c in special for c in password) < 1:
        password.append(secrets.choice(special))
    
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    user_input = input("Enter desired password length (at least 8) or a base password: ")
    
    try:
        password_length = int(user_input)
        strong_password = generate_password(password_length)
        print(f"Your generated password is: {strong_password}")
    except ValueError:
        try:
            strengthened_password = strengthen_password(user_input)
            print(f"Your strengthened password is: {strengthened_password}")
        except ValueError as e:
            print(f"Error: {e}")