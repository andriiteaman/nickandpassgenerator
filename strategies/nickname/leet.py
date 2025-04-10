import random


class Leet:
    def __init__(self):
        self.replaceable_letters = ['a', 'e', 'i', 'o', 's', 't']
        self.replacement_map = {
            'a': '4',
            'e': '3',
            'i': '1',
            'o': '0',
            's': '5',
            't': '7'
        }

    def generate(self, nickname_list):
        nickname = random.choice(nickname_list)

        if not any(letter in nickname.lower() for letter in self.replaceable_letters):
            return nickname

        nickname_list = list(nickname)

        num_replacements = random.randint(1, len(nickname_list))

        for _ in range(num_replacements):
            letter_to_replace = random.choice(self.replaceable_letters)

            for i, char in enumerate(nickname_list):
                if char.lower() == letter_to_replace:
                    nickname_list[i] = self.replacement_map[letter_to_replace]
                    break

        new_nickname = ''.join(nickname_list)
        return new_nickname
