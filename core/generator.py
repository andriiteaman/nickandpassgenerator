import random
import importlib
import os
import inspect
import string
from core.theme_loader import ThemeLoader

class Generator:
    def __init__(self, theme_loader: ThemeLoader, nickname_strategies_dir='strategies/nickname', password_strategies_dir='strategies/password'):
        self.theme_loader = theme_loader
        self.nickname_strategies = self.load_strategies(nickname_strategies_dir)
        self.password_strategies = self.load_strategies(password_strategies_dir)

    def load_strategies(self, strategies_dir):
        strategies = []
        for filename in os.listdir(strategies_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                strategy_name = filename[:-3]
                module = importlib.import_module(f'strategies.{strategies_dir.split("/")[-1]}.{strategy_name}')

                strategy_class = getattr(module, strategy_name.capitalize())

                # Get constructor parameters for the strategy class
                sig = inspect.signature(strategy_class)
                params = sig.parameters

                # If the strategy requires additional arguments (e.g., word_list)
                if 'word_list' in params:
                    word_list = self.theme_loader.get_all_themes()  # Example, adjust as needed
                    strategies.append(strategy_class(word_list))  # Pass word_list to the strategy constructor
                elif 'theme_loader' in params:
                    strategies.append(strategy_class(self.theme_loader))  # Pass theme_loader to the strategy constructor
                else:
                    strategies.append(strategy_class())  # No additional parameters, create the strategy normally
        return strategies

    def generate_nickname(self, theme):
        words = self.theme_loader.get_words_for_theme(theme)
        if not words:
            words = [theme]

        chosen_strategy = random.choice(self.nickname_strategies)
        nickname = chosen_strategy.generate(words)
        nickname = nickname.replace(' ', '_')

        # Перевірка довжини ніку
        if len(nickname) < 5:
            additional_chars = random.choices(string.ascii_letters + string.digits, k=5)
            nickname += ''.join(additional_chars)

        if len(nickname) > 30:
            nickname = nickname[:30]
        print(f"  Chosen Strategy: {chosen_strategy.__class__.__name__}")
        return nickname

    def generate_password(self, nickname):
        chosen_strategy = random.choice(self.password_strategies)
        print(f"  Chosen Strategy for Password: {chosen_strategy.__class__.__name__}")

        if 'nickname' in inspect.signature(chosen_strategy.generate).parameters:
            password = chosen_strategy.generate(nickname)  # Pass nickname if required
        elif 'nickname_list' in inspect.signature(chosen_strategy.generate).parameters:
            password = chosen_strategy.generate(nickname)
        elif 'words' in inspect.signature(chosen_strategy.generate).parameters:
            password = chosen_strategy.generate(nickname)
        else:
            password = chosen_strategy.generate()  # No nickname needed, just generate the password

        password = self.ensure_password_compliance(password)  # Ensure the password meets the requirements
        return password

    def ensure_password_compliance(self, password):
        self.length = 12
        self.digits = string.digits  # Digits (0-9)
        self.special_characters = "!@#$%^&*()-_=+"  # Special characters

        # Check minimum length (at least 8 characters, ideally 12-16 characters)
        while len(password) < 8:
            password += random.choice(self.digits + self.special_characters)  # Add random characters to meet the length

        # Ensure at least one lowercase letter, one uppercase letter, one digit, and one special character
        while not any(c.islower() for c in password):
            password += random.choice(string.ascii_lowercase)
        while not any(c.isupper() for c in password):
            password += random.choice(string.ascii_uppercase)
        while not any(c.isdigit() for c in password):
            password += random.choice(self.digits)
        while not any(c in self.special_characters for c in password):
            password += random.choice(self.special_characters)

        # Replace spaces with underscores
        password = password.replace(" ", "_")

        # Replace simple sequences (like '123', 'abc', 'password')
        simple_sequences = ['123', 'abc', 'password', 'qwerty']
        for seq in simple_sequences:
            if seq in password:
                password = password.replace(seq, random.choice(self.digits + self.special_characters))

        # Trim to the required length if it exceeds the limit
        if len(password) > self.length:
            password = password[:self.length]

        return password

if __name__ == '__main__':
    theme_loader = ThemeLoader()
    theme_loader.load_themes()
    theme = random.choice(theme_loader.get_all_themes())
    print(theme)
    generator = Generator(theme_loader)

    nickname = generator.generate_nickname(theme)
    password = generator.generate_password(theme)

    print(f"Nickname: {nickname} | Password: {password}")
