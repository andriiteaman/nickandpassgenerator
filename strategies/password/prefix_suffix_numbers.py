import random

class Prefix_suffix_numbers:
    def __init__(self):
        pass

    def generate(self, nickname):
        # Генеруємо випадкову кількість цифр для префікса та суфікса (від 1 до 4)
        num_prefix = random.randint(1, 4)
        num_suffix = random.randint(1, 4)

        prefix = ''.join(random.choices('0123456789', k=num_prefix))
        suffix = ''.join(random.choices('0123456789', k=num_suffix))

        # Додаємо префікс та суфікс до нікнейму
        new_nickname = prefix + nickname + suffix
        return new_nickname
