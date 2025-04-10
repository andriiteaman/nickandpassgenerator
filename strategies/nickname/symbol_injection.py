import random


class Symbol_injection:
    def __init__(self):
        self.symbols = ['!', '@', '#', '$', '%', '^', '*', '(', ')', '-', '_', '=', '+']

    def generate(self, nickname_list):

        nickname = random.choice(nickname_list)
        num_symbols = random.randint(1, 5)

        symbols_to_insert = random.choices(self.symbols, k=num_symbols)

        nickname_list = list(nickname)

        for symbol in symbols_to_insert:
            position = random.randint(0, len(nickname_list))
            nickname_list.insert(position, symbol)

        new_nickname = ''.join(nickname_list)
        return new_nickname