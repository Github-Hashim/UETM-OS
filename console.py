"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""
import os  # Import the 'os' module for system-related functions
import sys  # Import the 'sys' module for system-related functions
import run_applications  # Import your custom 'run_applications' module

def display_console_menu():
    while True:
        # Display the console menu options
        print("Please select an option:")
        print("1 to Run Applications")
        print("2 to Exit")

        # Get user input for the menu choice
        choice1 = int(input())

        # Clear the console screen
        os.system("cls")

        if choice1 == 1:
            # Call the 'run_applications' function from your custom module
            run_applications.run_applications()
        elif choice1 == 2:
            # Exit the program
            sys.exit()
        else:
            print("Wrong Input Provided.")
