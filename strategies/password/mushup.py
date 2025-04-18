import random


class Mushup:
    def generate(self, words):
        if len(words) < 2:
            return "".join(words)

        word1 = random.choice(words)
        word2 = random.choice(words)

        while word1 == word2:
            word2 = random.choice(words)

        combine_strategy = random.choice(['cut', 'insert'])

        if combine_strategy == 'cut':
            if len(word1) > 1 and len(word2) > 1:
                split_index1 = random.randint(1, len(word1) - 1)
                split_index2 = random.randint(1, len(word2) - 1)

                part1 = word1[:split_index1]
                part2 = word2[split_index2:]

                mashup_word = part1 + part2
            else:
                return word1 + word2

        else:
            if len(word1) > 1 and len(word2) > 1:
                insert_index = random.randint(1, len(word1) - 1)
                mashup_word = word1[:insert_index] + word2 + word1[insert_index:]
            else:
                return word1 + word2

        return mashup_word


if __name__ == "__main__":
    words = ["matrix", "glitch", "hacker", "cyber", "root", "admin"]

    mashup_strategy = Mushup()

    nickname = mashup_strategy.generate(words)

    print(f"Nickname: {nickname}")
