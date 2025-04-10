import random


class Symbol_injection:
    def __init__(self):
        self.symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '?', '/', '\\']

    def generate(self, nickname):
        # Визначаємо випадкову кількість символів для вставки (від 1 до 5)
        num_symbols = random.randint(1, 5)

        # Генеруємо список випадкових символів
        symbols_to_insert = random.choices(self.symbols, k=num_symbols)

        # Перетворюємо слово в список символів для зручнішої вставки
        nickname_list = list(nickname)

        # Визначаємо кількість місць для вставки
        for symbol in symbols_to_insert:
            # Вибираємо випадкову позицію для вставки символу
            position = random.randint(0, len(nickname_list))
            nickname_list.insert(position, symbol)

        # Перетворюємо список назад у рядок
        new_nickname = ''.join(nickname_list)
        return new_nickname