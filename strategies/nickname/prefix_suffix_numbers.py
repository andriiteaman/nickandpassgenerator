import random

class Prefix_suffix_numbers:
    def __init__(self):
        pass

    def generate(self, nickname):
        # Вибір випадкового слова з списку слів (nickname)
        chosen_word = random.choice(nickname)

        # Генеруємо випадкову кількість цифр для префікса та суфікса (від 1 до 4)
        num_prefix = random.randint(1, 4)
        num_suffix = random.randint(1, 4)

        prefix = ''.join(random.choices('0123456789', k=num_prefix))
        suffix = ''.join(random.choices('0123456789', k=num_suffix))

        # Додаємо префікс та суфікс до вибраного слова
        new_nickname = prefix + chosen_word + suffix
        return new_nickname
