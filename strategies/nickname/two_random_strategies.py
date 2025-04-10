import random
from strategies.nickname.leet import Leet
from strategies.nickname.reverse import Reverse
from strategies.nickname.mushup import Mushup
from strategies.nickname.prefix_suffix_numbers import Prefix_suffix_numbers
from strategies.nickname.symbol_injection import Symbol_injection
from strategies.nickname.theme_mushup import Theme_mushup

class Two_random_strategies:
    def __init__(self, theme_loader):
        self.strategies = [
            Leet(),
            Reverse(),
            Mushup(),
            Prefix_suffix_numbers(),
            Symbol_injection(),
            Theme_mushup(theme_loader)
        ]

    def generate(self, nickname):
        strategy1, strategy2 = random.sample(self.strategies, 2)

        modified_nickname = strategy1.generate(nickname)

        final_nickname = strategy2.generate(modified_nickname)

        return final_nickname