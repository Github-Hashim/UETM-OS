"""
Author: Muhammad Hashim
Dated: September 27, 2023
"""

# Importing custom-made modules and predefined modules
import credentials  # Custom-made module for handling credentials
import logo  # Custom-made module for displaying a logo
import timestamp  # Custom-made module for displaying the current date and time
import os  # Predefined module for clearing the console screen
import console  # Custom-made module for displaying the console menu

# Displaying the lab information and author
logo.draw_logo()

# Displaying any credentials (e.g., login information)
if credentials.credentials() == True:
    os.system('cls')    #clear the console creen3
    print("Login Successfully! Welcome.")

# Displaying the current date and time
timestamp.display_timestamp()

# Displaying the console menu
console.display_console_menu()


