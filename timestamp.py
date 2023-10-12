"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""

import datetime  # Import the 'datetime' module for date and time handling

def display_timestamp():
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Display the current date and time in a formatted string
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')

    # Print the formatted timestamp
    print(f"Current Date and Time: {formatted_datetime}")
