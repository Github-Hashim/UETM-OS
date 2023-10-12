"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""

import turtle as t  # Import the turtle graphics library and alias it as 't'

# Define a function to draw text
def draw_text(text, font_size, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text, align="center", font=("Arial", font_size, "bold"))  # Write text with specified font and alignment

def draw_logo(): 
    # Set up the Turtle screen
    t.bgcolor("White")  # Set the background color to white
    t.title("UETM OS Logo")  # Set the window title
    t.speed(1)  # Set the drawing speed

    # Draw "UETM OS" text
    text = "UETM OS"
    text_size = 36  # Adjust the font size as needed
    draw_text(text, text_size, 0, -50)  # Draw the text at coordinates (0, -50)

    # Hide the Turtle
    t.hideturtle()
    # Close the Turtle graphics window when clicked
    t.exitonclick()
