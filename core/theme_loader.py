import os

class ThemeLoader:
    def __init__(self, themes_file='../data/themes.txt', words_dir='../data/theme_words/'):
        # Шляхи до файлів і директорій
        self.themes_file = themes_file
        self.words_dir = words_dir
        self.themes = []
        self.theme_words = {}

    def load_themes(self):
        """Завантажує список тем із файлу themes.txt"""
        try:
            with open(self.themes_file, 'r', encoding='utf-8') as file:
                self.themes = [line.strip() for line in file.readlines()]
            print(f"Завантажено {len(self.themes)} тем.")
            return self.themes
        except FileNotFoundError:
            print(f"Файл {self.themes_file} не знайдено.")
        except Exception as e:
            print(f"Помилка при завантаженні тем: {e}")

    def load_theme_words(self, theme):
        """Завантажує слова по конкретній темі зі спеціального файлу"""
        theme_file = os.path.join(self.words_dir, f"{theme}.txt")
        words = []
        if os.path.exists(theme_file):
            try:
                with open(theme_file, 'r', encoding='utf-8') as file:
                    words = [line.strip() for line in file.readlines()]
                print(f"Завантажено {len(words)} слів для теми '{theme}'.")
            except Exception as e:
                print(f"Помилка при завантаженні слів для теми '{theme}': {e}")
        else:
            print(f"Файл для теми '{theme}' не знайдено.")
        return words

    def get_all_themes(self):
        """Повертає всі доступні теми"""
        return self.themes

    def get_words_for_theme(self, theme):
        """Повертає слова для конкретної теми"""
        if theme not in self.theme_words:
            # Завантажуємо слова для теми, якщо ще не були завантажені
            words = self.load_theme_words(theme)
            self.theme_words[theme] = words
        return self.theme_words.get(theme, [])

    def get_all_words(self):
        """Повертає всі слова для всіх тем як список списків"""
        all_words = {}
        for theme in self.themes:
            words = self.get_words_for_theme(theme)
            if words:
                all_words[theme] = words
        return all_words

# Приклад використання
if __name__ == '__main__':
    theme_loader = ThemeLoader()
    theme_loader.load_themes()  # Завантажуємо теми

    # Приклад 1: Отримання всіх тем
    all_themes = theme_loader.get_all_themes()
    print(f"All themes: {all_themes}")

    # Приклад 2: Отримання всіх слів для конкретної теми
    theme = 'hacking'  # Приклад теми
    words = theme_loader.get_words_for_theme(theme)
    print(f"Words for theme '{theme}': {words}")

    # Приклад 3: Отримання всіх слів для всіх тем
    all_words = theme_loader.get_all_words()
    print(f"All words: {all_words}")
