import random

class Theme_mushup:
    def __init__(self, theme_loader):
        self.theme_loader = theme_loader

    def generate(self):
        # Завантажуємо список всіх тем через метод get_all_themes()
        themes = self.theme_loader.get_all_themes()

        # Вибираємо дві різні теми випадковим чином
        theme1, theme2 = random.sample(themes, 2)

        # Завантажуємо слова для кожної з тем за допомогою методу get_words_for_theme
        words_theme1 = self.theme_loader.get_words_for_theme(theme1)
        words_theme2 = self.theme_loader.get_words_for_theme(theme2)

        # Перевіряємо, чи є слова в кожній темі
        if not words_theme1 or not words_theme2:
            return None  # Якщо одна з тем не має слів, повертаємо None

        # Вибираємо випадкові слова з кожної теми
        word1 = random.choice(words_theme1)
        word2 = random.choice(words_theme2)

        # Комбінуємо їх у випадковому порядку
        mashup = random.choice([word1 + word2, word2 + word1])
        return mashup