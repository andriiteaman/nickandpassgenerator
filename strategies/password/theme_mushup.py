import random

class Theme_mushup:
    def __init__(self, theme_loader):
        self.theme_loader = theme_loader

    def generate(self, words):
        theme1_word = random.choice(words)
        theme2_word = random.choice(words)

        return theme1_word + theme2_word