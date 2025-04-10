import os
import importlib


class UtilityManager:
    def __init__(self, utils_directory="utils"):
        self.utils_directory = utils_directory  # The directory where utilities are stored

    def list_utilities(self):
        """Lists all Python utility scripts in the specified directory."""
        files = [f[:-3] for f in os.listdir(self.utils_directory) if f.endswith('.py') and f != '__init__.py']
        return files

    def execute_utility(self, utility_name):
        """Dynamically imports and executes the selected utility."""
        try:
            module = importlib.import_module(f'{self.utils_directory}.{utility_name}')
            if hasattr(module, 'run'):  # Check if the utility has a 'run' function
                module.run()  # Execute the utility's run function
            else:
                print(f"Error: Utility '{utility_name}' does not have a 'run' function.")
        except ModuleNotFoundError:
            print(f"Error: Utility '{utility_name}' not found.")
        except Exception as e:
            print(f"Error while executing utility '{utility_name}': {e}")

    def show_utilities_menu(self):
        """Displays the utility menu for the user to choose from."""
        print("\nSelect a utility from the list:")
        utilities = self.list_utilities()

        if not utilities:
            print("No utilities found!")
            return

        # Show the utilities available
        for i, utility in enumerate(utilities, 1):
            print(f"{i}. {utility}")

        print("0. Back to Main Menu")  # Option to go back to the main menu

        # Get the user's choice
        choice = input("Enter your choice (number): ")

        if choice == '0':
            return  # Go back to main menu
        elif choice.isdigit() and 1 <= int(choice) <= len(utilities):
            selected_utility = utilities[int(choice) - 1]
            self.execute_utility(selected_utility)
        else:
            print("Invalid choice! Please try again.")

    def run(self):
        """Main function to display the menu and handle utility execution."""
        self.show_utilities_menu()

if __name__ == "__main__":
    # Create an instance of the UtilityManager and run the utility menu
    utility_manager = UtilityManager()
    utility_manager.run()

