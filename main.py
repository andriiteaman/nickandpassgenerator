import random
import os
from core.theme_loader import ThemeLoader
from core.generator import Generator
from strategies.password.random_pass import Random_pass
from utilsmanager import UtilityManager
import time

# ---- Open Source Project Header ----
def print_header():
    print("""
    ╔════════════════════════════════════════════════════╗
    ║              Welcome to Nick & Pass Generator      ║
    ║                                                    ║
    ║     A fun and customizable tool for generating     ║
    ║     unique usernames and secure passwords.         ║
    ║     Easily extendable and open-source.             ║
    ║                                                    ║
    ║     By Andrii                                      ║
    ║     GitHub: https://github.com/andriicoder         ║
    ╚════════════════════════════════════════════════════╝
    """)

# ---- Function to Generate Nickname and Password ----
def generate_nickname_and_password():
    theme_loader = ThemeLoader()
    theme_loader.load_themes()  # Load all themes from the themes.txt file
    theme = random.choice(theme_loader.get_all_themes())  # Randomly choose a theme

    # Initialize the Generator from core/generator.py
    generator = Generator(theme_loader)


    # Generate Nickname and Password
    nickname = generator.generate_nickname(theme)
    password = generator.generate_password(nickname)
    print(f"  Selected Theme: {theme.capitalize()}")

    # Print the generated results
    print(f"\n{'=' * 50}")
    print(f"     Nickname & Password Generated  ")
    print(f"{'=' * 50}")
    print(f"\n     Nickname: {nickname}")
    print(f"     Password: {password}")
    print(f"\n{'=' * 50}\n")


def generate_random_password():
    # Create an instance of Random_pass to generate a password
    password_generator = Random_pass(length=12)  # Create an instance of Random_pass with 12 character length
    password = password_generator.generate()  # Generate the password using Random_pass

    # Print the result
    print(f"\n{'=' * 50}")
    print(f"     Random Password Generated  ")
    print(f"{'=' * 50}")
    print(f"\n     Password: {password}")
    print(f"\n{'=' * 50}\n")
# ---- Clear the Screen ----
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for Windows or Unix-based systems

# ---- Main Menu ----
def show_menu():
    print("\nSelect an option:")
    print("1. Generate Random Nickname and Password")
    print("2. Generate Random Password (Random Pass Strategy)")
    print("3. Utilities Manager")
    print("0. Exit")

# ---- Main Function ----
def main():
    utility_manager = UtilityManager()

    while True:
        print_header()
        show_menu()  # Show menu options
        choice = input("Enter your choice (1/2/3/0): ")

        if choice == '1':
            clear_screen()  # Clear the screen
            generate_nickname_and_password()  # Generate and display Nickname & Password
        elif choice == '2':
            clear_screen()  # Clear the screen
            generate_random_password()  # Generate and display Random Password (using Random_pass strategy)
        elif choice == '3':
            clear_screen()  # Clear the screen
            utility_manager.run()  # Call the utilities manager
        elif choice == '0':
            clear_screen()  # Clear the screen
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")
            time.sleep(1)  # Wait for 2 seconds before clearing screen and showing menu again
            clear_screen()  # Clear the screen for invalid input

# ---- Run the main program ----
if __name__ == "__main__":
    main()
