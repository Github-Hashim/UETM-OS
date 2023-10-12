"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""
import winsound  # Import the 'winsound' module for sound generation

def play_singer1_music():
    # Define the frequency and duration for Singer 1's music.
    frequency = 440  # Example frequency (440 Hz).
    duration = 1000  # Example duration (milliseconds).

    # Generate a beep sound with the specified frequency and duration
    winsound.Beep(frequency, duration)


def play_singer2_music():
    # Define the frequency and duration for Singer 2's music.
    frequency = 880  # Example frequency (880 Hz).
    duration = 800  # Example duration (milliseconds).

    # Generate a beep sound with the specified frequency and duration
    winsound.Beep(frequency, duration)
