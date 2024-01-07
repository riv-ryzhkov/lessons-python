import random
import string


def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    # You can customize the length of the password as needed
    password_length = int(input("Enter the desired length of the password: "))

    if password_length < 1:
        print("Password length should be at least 1.")
    else:
        generated_password = generate_password(password_length)
        print(f"Generated Password: {generated_password}")