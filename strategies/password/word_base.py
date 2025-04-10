import random
import string


class Word_base:
    def __init__(self, word_list, length=12):
        # Check if the password length is at least 8 characters
        if length < 8:
            raise ValueError("Password must be at least 8 characters long")

        self.length = length
        self.word_list = word_list  # List of words to choose from
        self.digits = string.digits  # digits (0-9)
        self.special_characters = "!@#$%^&*()-_=+"  # special characters

    def generate(self):
        # Randomly select a word from the list
        base_word = random.choice(self.word_list)

        # Randomly modify the case of the letters in the word
        modified_word = ''.join(random.choice([c.lower(), c.upper()]) for c in base_word)

        # Add random digits and special characters to meet the required length
        password = [modified_word]
        password += random.choices(self.digits + self.special_characters, k=self.length - len(modified_word))

        # Shuffle the characters to ensure randomness
        random.shuffle(password)

        # Convert the list of characters back into a string
        return ''.join(password)


# Ensure that the code is executed only when the script is run directly
if __name__ == "__main__":
    # Example word list, in a real case it would come from an external file or source
    word_list = ["dragon", "sunshine", "password", "wizard", "hacking", "octopus", "moonlight"]

    # Using the class to generate a password
    password_generator = Word_base(word_list, length=12)
    generated_password = password_generator.generate()

    # Print the generated password
    print("Generated Password:", generated_password)
