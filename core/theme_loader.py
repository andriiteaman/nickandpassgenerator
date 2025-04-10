import os

class ThemeLoader:
    def __init__(self, themes_file='../data/themes.txt', words_dir='../data/theme_words/'):
        self.themes_file = themes_file
        self.words_dir = words_dir
        self.themes = []
        self.theme_words = {}

    def load_themes(self):
        try:
            with open(self.themes_file, 'r', encoding='utf-8') as file:
                self.themes = [line.strip() for line in file.readlines()]
            print(f"Downloaded {len(self.themes)} themes.")
            return self.themes
        except FileNotFoundError:
            print(f"File {self.themes_file} not found.")
        except Exception as e:
            print(f"Error while downloading theme: {e}")

    def load_theme_words(self, theme):
        theme_file = os.path.join(self.words_dir, f"{theme}.txt")
        words = []
        if os.path.exists(theme_file):
            try:
                with open(theme_file, 'r', encoding='utf-8') as file:
                    words = [line.strip() for line in file.readlines()]
                print(f"Downloaded {len(words)} words for theme '{theme}'.")
            except Exception as e:
                print(f"Error while downloading theme '{theme}': {e}")
        else:
            print(f"File '{theme}' not found.")
        return words

    def get_all_themes(self):
        return self.themes

    def get_words_for_theme(self, theme):
        if theme not in self.theme_words:
            words = self.load_theme_words(theme)
            self.theme_words[theme] = words
        return self.theme_words.get(theme, [])

    def get_all_words(self):
        all_words = {}
        for theme in self.themes:
            words = self.get_words_for_theme(theme)
            if words:
                all_words[theme] = words
        return all_words

if __name__ == '__main__':
    theme_loader = ThemeLoader()
    theme_loader.load_themes()

    all_themes = theme_loader.get_all_themes()
    print(f"All themes: {all_themes}")

    theme = 'hacking'
    words = theme_loader.get_words_for_theme(theme)
    print(f"Words for theme '{theme}': {words}")

    all_words = theme_loader.get_all_words()
    print(f"All words: {all_words}")
