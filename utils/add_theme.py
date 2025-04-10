import os


def run():
    """Функція для додавання нової теми."""
    # Запит на введення шляху до файлу зі словами
    theme_file = input("Enter the path to the file with words (e.g., 'new_theme.txt'): ").strip()

    # Перевірка на існування файлу
    if not os.path.exists(theme_file):
        print(f"Error: File '{theme_file}' does not exist!")
        return

    # Перевірка, чи це текстовий файл
    if not theme_file.endswith('.txt'):
        print("Error: Only '.txt' files are allowed!")
        return

    # Читання слів з файлу
    try:
        with open(theme_file, 'r', encoding='utf-8') as file:
            words = file.readlines()
            words = [word.strip() for word in words if word.strip()]  # Видаляємо порожні рядки та пробіли
    except Exception as e:
        print(f"Error while reading the file: {e}")
        return

    # Перевірка на формат: кожне слово повинно бути на окремому рядку
    if not all(len(word.split()) == 1 for word in words):
        print("Error: Each line must contain exactly one word!")
        return

    # Додавання теми в themes.txt
    theme_name = os.path.splitext(os.path.basename(theme_file))[0]  # Використовуємо ім'я файлу як назву теми
    try:
        with open('data/themes.txt', 'a', encoding='utf-8') as themes_file:
            themes_file.write(f"{theme_name}\n")  # Додаємо назву теми в themes.txt

        # Додавання слів у директорію theme_words
        theme_words_dir = 'data/theme_words'
        os.makedirs(theme_words_dir, exist_ok=True)  # Створюємо директорію, якщо вона не існує
        theme_words_file = os.path.join(theme_words_dir, f"{theme_name}.txt")
        with open(theme_words_file, 'w', encoding='utf-8') as theme_file:
            for word in words:
                theme_file.write(f"{word}\n")  # Записуємо кожне слово на новому рядку

        print(f"Theme '{theme_name}' has been added successfully!")

    except Exception as e:
        print(f"Error while adding the theme: {e}")

