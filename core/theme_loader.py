import os

class ThemeLoader:
    def __init__(self, themes_file='data/themes.txt', words_dir='data/theme_words/'):
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

# Приклад використання
if __name__ == '__main__':
    theme_loader = ThemeLoader()
    theme_loader.load_themes()  # Завантажуємо теми
    theme = 'hacking'  # Приклад теми
    words = theme_loader.get_words_for_theme(theme)  # Завантажуємо слова для теми "hacking"
    print(words)