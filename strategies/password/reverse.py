import random


class Reverse:
    def generate(self, words):
        if not words:
            return ""

        word = random.choice(words)

        return word[::-1]