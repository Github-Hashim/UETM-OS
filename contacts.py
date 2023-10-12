"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""

import os  # Import the 'os' module to use operating system-related functions

# Define a global list to store contacts
contacts = [] #it will contains the contact list till the program termination

def phonebook():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. to back")
        choice = input("Enter your choice (1/2/3): ")

        # Clear the console screen
        os.system("cls")

        if choice == "1":
            # Get user input for contact details
            name = input("Enter name: ")
            contact_number = input("Enter contact number (+92 xxx-xxxxxxx): ")
            gender = input("Enter gender(Male/Female): ")
            address = input("Enter address: ")

            # Create a dictionary to store user information
            contact_info = {
                "Name": name,
                "Contact Number": contact_number,
                "Gender": gender,
                "Address": address,
            }

            # Add the contact to the list
            contacts.append(contact_info)

            # Clear the console screen
            os.system("cls")
            print("Contact added successfully!")

        elif choice == "2":
            if not contacts:
                # Clear the console screen
                os.system("cls")
                print("Phonebook is empty.")
            else:
                print("\nContact List:")
                print("-------------------------")
                # Loop through the list of contacts and display each contact's information
                for idx, contact in enumerate(contacts, start=1):
                    print(f"Contact {idx}:")
                    # Loop through the dictionary of contact information and display each key-value pair
                    for key, value in contact.items():
                        print(f"{key}: {value}")
                    print("-------------------------")

        elif choice == "3":
            print("Exiting Phonebook.")
            break

        else:
            print("Invalid choice. Please select a valid option (1/2/3).")
