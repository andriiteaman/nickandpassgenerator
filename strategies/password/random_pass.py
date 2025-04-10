import random
import string


class Random_pass:
    def __init__(self, length=12):
        # Check if the password length is at least 8 characters
        if length < 8:
            raise ValueError("Password must be at least 8 characters long")

        self.length = length
        self.lowercase_letters = string.ascii_lowercase  # lowercase letters (a-z)
        self.uppercase_letters = string.ascii_uppercase  # uppercase letters (A-Z)
        self.digits = string.digits  # digits (0-9)
        self.special_characters = "!@#$%^&*()-_=+"  # special characters

    def generate(self):
        # Generate the password with mandatory character types
        password = [
            random.choice(self.lowercase_letters),  # one lowercase letter
            random.choice(self.uppercase_letters),  # one uppercase letter
            random.choice(self.digits),  # one digit
            random.choice(self.special_characters),  # one special character
        ]

        # Add random characters to reach the desired password length
        all_characters = self.lowercase_letters + self.uppercase_letters + self.digits + self.special_characters
        password += random.choices(all_characters, k=self.length - 4)

        # Shuffle the characters to ensure randomness
        random.shuffle(password)

        # Convert the list of characters back into a string
        return ''.join(password)


# Ensure that the code is executed only when the script is run directly
if __name__ == "__main__":
    # Using the class to generate a password
    password_generator = PasswordGenerator(length=12)
    generated_password = password_generator.generate()

    # Print the generated password
    print("Generated Password:", generated_password)