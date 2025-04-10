import random

class Leet:
    def generate(self, words):
        leet_dict = {
            'a': '4', 'b': '8', 'c': '(', 'e': '3', 'f': 'ph', 'g': '9', 'h': '#',
            'i': '1', 'j': 'L', 'k': 'X', 'l': '1', 'm': 'M', 'n': '^', 'o': '0',
            'p': 'P', 'q': '9', 'r': '2', 's': '5', 't': '7', 'u': 'U', 'v': 'V',
            'w': 'VV', 'x': '%', 'y': 'Y', 'z': '2'
        }

        word = random.choice(words)

        word_list = list(word)

        replaceable_letters = [i for i, letter in enumerate(word_list) if letter.lower() in leet_dict]

        num_replacements = random.randint(1, len(replaceable_letters))

        indices_to_replace = random.sample(replaceable_letters, num_replacements)

        for idx in indices_to_replace:
            letter = word_list[idx].lower()
            word_list[idx] = leet_dict.get(letter, word_list[idx])

        return ''.join(word_list)

