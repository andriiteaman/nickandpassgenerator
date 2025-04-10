import random
import importlib
import os
import inspect
from core.theme_loader import ThemeLoader

class Generator:
    def __init__(self, theme_loader: ThemeLoader, nickname_strategies_dir='../strategies/nickname', password_strategies_dir='../strategies/password'):
        self.theme_loader = theme_loader
        self.nickname_strategies = self.load_strategies(nickname_strategies_dir)
        self.password_strategies = self.load_strategies(password_strategies_dir)

    def load_strategies(self, strategies_dir):
        strategies = []
        for filename in os.listdir(strategies_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                strategy_name = filename[:-3]
                # Заміна шляху на правильний формат пакету
                module = importlib.import_module(f'strategies.{strategies_dir.split("/")[-1]}.{strategy_name}')

                # Отримуємо клас стратегії
                strategy_class = getattr(module, strategy_name.capitalize())

                # Використовуємо inspect для перевірки, чи потребує клас параметр 'theme_loader' в __init__
                sig = inspect.signature(strategy_class)
                params = sig.parameters
                if 'theme_loader' in params:
                    # Якщо клас вимагає 'theme_loader', передаємо його
                    strategies.append(strategy_class(self.theme_loader))
                else:
                    # Для інших стратегій створюємо без додаткових аргументів
                    strategies.append(strategy_class())
        return strategies

    def generate_nickname(self, theme):
        words = self.theme_loader.get_words_for_theme(theme)
        if not words:
            words = [theme]

        chosen_strategy = random.choice(self.nickname_strategies)

        nickname = chosen_strategy.generate(words)
        return nickname

    def generate_password(self, nickname, theme):
        chosen_strategy = random.choice(self.password_strategies)

        # Передаємо тільки два аргументи: nickname та self
        password = chosen_strategy.generate(nickname)  # Оновлений виклик
        return password

if __name__ == '__main__':
    theme_loader = ThemeLoader()
    theme_loader.load_themes()
    theme = random.choice(theme_loader.get_all_themes())
    print(theme)
    generator = Generator(theme_loader)

    nickname = generator.generate_nickname(theme)
    password = generator.generate_password(nickname, theme)

    print(f"Nickname: {nickname} | Password: {password}")
