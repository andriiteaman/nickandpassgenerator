import random

class Theme_mushup:
    def __init__(self, theme_loader):
        self.theme_loader = theme_loader

    def generate(self, words):
        # Реалізація стратегії для комбінування частин слів
        theme1_word = random.choice(words)
        theme2_word = random.choice(words)

        # Комбінуємо два слова з теми
        return theme1_word + theme2_word