Password Generator using Python
Introduction

This Python script is a simple yet powerful password generator that creates random passwords based on user-defined preferences. It allows users to customize the strength and character set of the password to meet their security needs.
Features

    Password Strength Levels:
        Weak: Contains only lowercase letters.
        Okay: Includes lowercase, uppercase letters, and digits.
        Strong: Includes letters, digits, and special characters.
        Custom: Allows users to select their own character set.

    Interactive User Interface:
        Users can choose the type and length of the password.
        For the custom option, users can add letters, digits, and special characters to their character set interactively.

    Dynamic Display:
        The program uses terminal commands to clear the screen and create a clean, organized user interface.

Getting Started
Prerequisites

    Python 3.x installed on your system.

Running the Script

    Download or copy the script to your local machine.
    Open a terminal or command prompt.
    Run the script using the command:

    python password_generator.py

How to Use

    Select Password Strength:
    Upon running the script, you will be prompted to choose from one of the following options:
        Weak (Option 1)
        Okay (Option 2)
        Strong (Option 3)
        Custom (Option 4)

    Specify Password Length:
    Enter the desired length of your password.

    (Custom Option Only) Choose Character Sets:
        Add letters, digits, or special characters to your custom character set.
        You must select at least one character set before exiting.

    View Generated Password:
    The script will display your new randomly generated password.

Code Overview
Modules Used

    string: Provides predefined sets of characters like letters, digits, and punctuation.
    random: Used to generate random selections from the chosen character set.

Key Sections

    Password Strength Selection:
        Determines the character set based on user input.

    Custom Character Set:
        Allows users to build their own character set interactively.

    Password Generation:
        Creates a password by randomly selecting characters from the defined character set.

    Display and UI:
        Uses escape sequences (\033) to create a dynamic and colorful interface.
