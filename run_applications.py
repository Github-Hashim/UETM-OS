"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""
import os  # Import the 'os' module for system-related functions
import timestamp  # Import your custom 'timestamp' module
import sys  # Import the 'sys' module for system-related functions
import contacts  # Import your custom 'contacts' module
import hangmanGame  # Import your custom 'hangmanGame' module
import tictactoe  # Import your custom 'tictactoe' module
import music  # Import your custom 'music' module
import calculator  # Import your custom 'calculator' module
import mycalender  # Import your custom 'mycalender' module

def run_applications():
    while True:
        timestamp.display_timestamp()
        print("Please select anyone: ")
        print("1 for Menu")
        print("2 for exit")
        
        # Get user input for the main menu choice
        choice2 = int(input())
        os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)

        if choice2 == 1:
            while True:
                timestamp.display_timestamp()
                print("\t\t\tMain Menu\t\t\t")
                print("Press: ")
                print("1 for Phone Book")
                print("2 for Applications")
                print("3 for Games")
                print("4 for Music")
                print("5 for Exit")
                print("6 for Back")
                
                # Get user input for the submenu choice
                choice3 = int(input())
                os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)

                if choice3 == 1:
                    while True:
                        print("Press:")
                        print("1 for Phonebook.")
                        print("2 to back to main Menu")
                        print("3 to exit")
                        
                        # Get user input for the Phonebook submenu
                        option = int(input())
                        os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)

                        if option == 1:
                            contacts.phonebook()  # Call the 'phonebook' function from custom module
                            print("Press enter to go back to the main menu: ", end="")
                            button = input()
                            os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)
                            break
                        elif option == 2:
                            break
                        elif option == 3:
                            sys.exit()
                        else:
                            print("Wrong input provided.")

                elif choice3 == 2:
                    while True:
                        print("Press: ")
                        print("1 for calendar.")
                        print("2 for calculator.")
                        print("3 to back to menu.")
                        print("4 to exit.")
                        
                        # Get user input for the Applications submenu
                        option = int(input())
                        os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)

                        if option == 1:
                            mycalender.mycalendar()  # Call the 'mycalendar' function from your custom module
                            print("Press enter to go back to the main menu.")
                            temp = input()
                            os.system('cls')  # Clear the console screen on Windows (adjust for other platforms)
                            break
                        elif option == 2:
                            calculator.calculator()  # Call the 'calculator' function from your custom module
                            print("Press enter to go back to the main menu.")
                            temp = input()
                            os.system('cls')  # Clear the console screen on Windows (adjust for other platforms)
                            break
                        elif option == 3:
                            break
                        elif option == 4:
                            sys.exit()
                        else:
                            print("Wrong input provided.")

                elif choice3 == 3:
                    while True:
                        print("Press:")
                        print("1 to play HANGMAN")
                        print("2 to play TIC TAC TOE")
                        print("3 to go back to main menu")
                        print("4 to exit")
                        
                        # Get user input for the Games submenu
                        option = int(input())
                        os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)

                        if option == 1:
                            hangmanGame.hangman()  # Call the 'hangman' function from your custom module
                            print("Press enter to go back to the main menu: ", end="")
                            button = input()
                            os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)
                            break
                        elif option == 2:
                            tictactoe.tic_tac_toe()  # Call the 'tic_tac_toe' function from your custom module
                            print("Press enter to go back to the main menu: ", end="")
                            button = input()
                            os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)
                            break
                        elif option == 3:
                            break
                        elif option == 4:
                            sys.exit()
                        else:
                            print("Wrong input provided.")

                elif choice3 == 4:
                    while True:
                        print("Press:")
                        print("1 to listen to singer1 music")
                        print("2 to listen to singer2 music")
                        print("3 to go back to main menu")
                        print("4 to exit")
                        
                        # Get user input for the Music submenu
                        option = int(input())
                        os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)

                        if option == 1:
                            music.play_singer1_music()  # Call the 'play_singer1_music' function from your custom module
                            print("Press enter to go back to the main menu: ", end="")
                            button = input()
                            os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)
                            break
                        elif option == 2:
                            music.play_singer2_music()  # Call the 'play_singer2_music' function from your custom module
                            print("Press enter to go back to the main menu: ", end="")
                            button = input()
                            os.system("cls")  # Clear the console screen on Windows (adjust for other platforms)
                            break
                        elif option == 3:
                            break
                        elif option == 4:
                            sys.exit()
                        else:
                            print("Wrong input provided.")

                elif choice3 == 5:
                    sys.exit()
                elif choice3 == 6:
                    os.system("cls")
                    break
                else:
                    print("Wrong input provided.")

        elif choice2 == 2:
            sys.exit()
        else:
            print("Wrong input provided.")
