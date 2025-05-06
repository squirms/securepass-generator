import random
import string

def generate_password(length=12, use_specials=True):
    chars = string.ascii_letters + string.digits
    if use_specials:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Random Password Generator")
    try:
        length = int(input("Enter desired password length (default 12): ") or 12)
        use_specials = input("Include special characters? (y/n): ").lower().startswith('y')
        print("Generated password:", generate_password(length, use_specials))
    except ValueError:
        print("Invalid input. Please enter a number.")
