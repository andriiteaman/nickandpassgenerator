import random
from strategies.nickname.leet import Leet
from strategies.nickname.reverse import Reverse
from strategies.nickname.mushup import Mushup
from strategies.nickname.prefix_suffix_numbers import Prefix_suffix_numbers
from strategies.nickname.symbol_injection import Symbol_injection
from strategies.nickname.theme_mushup import Theme_mushup

class Two_random_strategies:
    def __init__(self, theme_loader):
        # Ініціалізація доступних стратегій
        self.strategies = [
            Leet(),
            Reverse(),
            Mushup(),
            Prefix_suffix_numbers(),
            Symbol_injection(),
            Theme_mushup(theme_loader)
        ]

    def generate(self, nickname):
        # Вибір двох випадкових стратегій
        strategy1, strategy2 = random.sample(self.strategies, 2)

        # Викликаємо першу стратегію
        modified_nickname = strategy1.generate(nickname)  # Передаємо лише 1 аргумент

        # Викликаємо другу стратегію
        final_nickname = strategy2.generate(modified_nickname)  # Передаємо лише 1 аргумент

        return final_nickname