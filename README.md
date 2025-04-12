# Nick & Pass Generator

## Overview
**Nick & Pass Generator** is a fun and customizable tool that helps generate unique usernames and secure passwords. It is easily extendable and open-source, designed to be a flexible solution for generating unique credentials for any application.

### Key Features:
- Random theme-based username generation
- Secure password generation with random characters, digits, and symbols
- Extendable with more themes and password generation strategies
- Easily customizable for your own requirements

## How It Works

### 1. **Theme Selection**
The program starts by randomly selecting a theme from a list of predefined themes. The themes can be anything from "Hacking" to "Fantasy," and each theme comes with a specific list of related words that are used to generate the username.

### 2. **Username Generation**
The program randomly applies various strategies to generate a unique username. These strategies include:
- Replacing letters with numbers or symbols (e.g., 'o' becomes '0')
- Reversing the word
- Combining pieces of words together
- Adding random numbers or special characters

### 3. **Password Generation**
Once the username is created, a password is generated using several strategies:
- Combining characters from the generated username
- Adding random symbols, digits, and upper/lowercase letters
- Ensuring that the password is complex and secure by meeting common password requirements

### 4. **Extending the Generator**
You can add more themes and strategies to the generator to suit your needs. Simply create a new theme file in the `data/` folder, and the program will automatically load it.

## Features for Utilities:
1. **Add New Themes**: Easily add new themes by providing a text file of words associated with the theme.
2. **Utilities Management**: The utility manager allows you to manage different utilities that can be run, including adding new themes, and viewing or editing the theme list.

## Setup

### Requirements:
- Python 3.x
- Dependencies:
  - `os`
  - `random`
  - `string`

### Installing:
1. Clone the repository or download the files.
2. Make sure all required dependencies are installed.

```bash
pip install -r requirements.txt
```

### Running the Program:
Simply run the `main.py` file to start the Nick & Pass Generator:

```bash
python main.py
```

## Example Output:

```
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

Select an option:
1. Generate Random Nickname and Password
2. Generate Random Password (Random Pass Strategy)
3. Utilities Manager
0. Exit
```

### Example Output for Generated Username and Password:

```
Selected Theme: hacking
==================================================
     Nickname & Password Generated
==================================================

     Nickname: 5Obi2
     Password: POSt_aPocALy
==================================================
```

## Customization:
Feel free to add your own themes and strategies:
1. Create a text file with words for a theme and place it in the `data/` folder.
2. Add your own strategy in the `strategies/nickname` or `strategies/password` directories.

### Possible Unique Username Combinations:
With the current setup and strategies, the total number of possible unique username combinations is approximately **37,740,652,036,012,307,457,000**.

## Contribution
If you would like to contribute or suggest new features, please feel free to fork the repository and submit a pull request!

### License
This project is open-source and released under the MIT License.

## Contact
For any questions or feedback, please contact me at **andriicoder@gmail.com** or visit the [GitHub Repository](https://github.com/andriicoder).
```
