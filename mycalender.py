"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""


import calendar  # Import the 'calendar' module for calendar generation

def mycalendar():
    # Get user input for the year and month
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    # Generate a calendar for the specified year and month
    cal = calendar.month(year, month)

    # Print the generated calendar
    print("\n", cal)
