import random

class Prefix_suffix_numbers:
    def __init__(self):
        pass

    def generate(self, nickname):
        chosen_word = random.choice(nickname)

        num_prefix = random.randint(1, 4)
        num_suffix = random.randint(1, 4)

        prefix = ''.join(random.choices('0123456789', k=num_prefix))
        suffix = ''.join(random.choices('0123456789', k=num_suffix))

        new_nickname = prefix + chosen_word + suffix
        return new_nickname
