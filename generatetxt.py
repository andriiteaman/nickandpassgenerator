import os

THEMES_FILE = 'data/themes.txt'
THEME_WORDS_DIR = 'data/theme_words/'

def create_theme_word_files():
    # Переконайся, що папка існує
    os.makedirs(THEME_WORDS_DIR, exist_ok=True)

    # Зчитування тем
    with open(THEMES_FILE, 'r', encoding='utf-8') as f:
        themes = [line.strip() for line in f if line.strip()]

    # Створення .txt файлів
    for theme in themes:
        filename = os.path.join(THEME_WORDS_DIR, f'{theme}.txt')
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as tf:
                tf.write('')  # Пустий файл
            print(f'[+] Created: {filename}')
        else:
            print(f'[!] Already exists: {filename}')

if __name__ == '__main__':
    create_theme_word_files()
