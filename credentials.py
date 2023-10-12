"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""

def credentials():
    while True:
        # Hardcoded username and password
        correct_username = "Muhammad Hashim"
        correct_password = "Hashim160"

        # Get user input for username and password
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        # Check if the entered username and password match the hardcoded values
        if input_username == correct_username and input_password == correct_password:
            return True
        else:
            # Failed login message
            print("Login failed. Please check your username and password and re-enter the valid one.")
