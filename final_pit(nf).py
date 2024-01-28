# This program is a color filling program created by SALAS and BONIOR
import time
import turtle
from turtle import Turtle, Screen
turtle.screensize(20, 20, "white")
screen = Screen()
pen = turtle
pen.shape("turtle")
pen.color("black")
pen.pensize(5)
pen.hideturtle()

text1 = ("\nWELCOME TO THE BEAR STATION"
         "\nLET'S FILL SOME BABY'S UP!!!!!")
for char in text1:
    print(char, end='', flush=True)
    time.sleep(0.1)


class BearParts:
    # The coordinates for the feet of the teddy bear
    # The Circle Shape for the feet of the teddy bear
    pen.penup()
    pen.goto(-155, -190)
    pen.down()
    pen.circle(radius=60)
    # Circle 2
    pen.penup()
    pen.goto(155, -190)
    pen.down()
    pen.circle(radius=60)
    pen.speed(10)
    # The coordinates for the body
    pen.penup()
    pen.goto(0, -190)
    pen.down()
    pen.circle(radius=150)
    pen.speed(10)
    # The coordinates for the head
    pen.penup()
    pen.goto(0, 110)
    pen.down()
    pen.circle(radius=80)
    pen.speed(10)
    # The coordinates for the ears
    # Ear 1
    pen.penup()
    pen.goto(100, 195)
    pen.down()
    pen.circle(radius=50)
    pen.speed(10)
    # Ear 2
    pen.penup()
    pen.goto(-100, 195)
    pen.down()
    pen.circle(radius=50)
    pen.speed(10)
    # The coordinates for the hands
    # Hand 1
    pen.penup()
    pen.goto(100, -50)
    pen.down()
    pen.circle(radius=60)
    pen.speed(10)
    # Hand 2
    pen.penup()
    pen.goto(-100, -50)
    pen.down()
    pen.circle(radius=60)
    pen.speed(10)


# Defining the Colors for the primary color
def color_choice(choice):
    if choice == 1:
        print("RED")
    elif choice == 2:
        print("YELLOW")
    elif choice == 3:
        print("BLUE")
    else:
        print("Input invalid.Refer from the choices.")


while True:
    text3 = "\n****Select your primary color****"
    for char in text3:
        print(char, end='', flush=True)
        time.sleep(0.050)

    choices = eval(input("\nFor RED press [1]"
                         "\nFor YELLOW press [2]"
                         "\nFor BLUE press [3]"
                         "\nEnter here:"))
    print("The primary color is ", end='')
    color_choice(choices)
    if choices == "Input invalid.Refer from the choices":
        break
    elif choices != "Input invalid.Refer from the choices":
        continue

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    # Secondary color selection
    text4 = "\n*****Select your secondary color*****"
    for char in text4:
        print(char, end='', flush=True)
        time.sleep(0.050)

    color2 = int(input("\nPress 5 for GREEN"
                       "\nPress 6 for ORANGE "
                       "\nPress 7 for PURPLE"
                       "\nEnter here:"))
    if color2 == 5:
        print("You have selected GREEN ")
    elif color2 == 6:
        print("You have selected ORANGE ")
    elif color2 == 7:
        print("You have selected PURPLE ")
    else:
        print("The input is invalid, refer to the choices.")

    print("\n=================================================="
          "\n-----THE RESULT OF THE COLORS YOU HAVE CHOSEN-----"
          "\n==================================================")

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    text5 = "\nThe tertiary result is:"
    for char in text5:
        print(char, end='', flush=True)
        time.sleep(0.050)

    # Combining two variables by multiplying the number inputs of the user
    inputs = choices * color2

    if inputs == 5:
        print("YELLOW\nColor Code: #FFFF00")
    elif inputs == 6:
        print("VERMILION\nColor code: #E34234")
    elif inputs == 7:
        print("MAGENTA/RED-VIOLET\nColor code: #C71585")
    elif inputs == 10:
        print("YELLOW-GREEN"
              "\nColor code: #9ACD32")
    elif inputs == 12:
        print("AMBER"
              "\nColor code: #FFBF00")
    elif inputs == 14:
        print("BROWN"
              "\nColor code: #964B00")
    elif inputs == 15:
        print("TEAL"
              "\nColor code: #008080")
    elif inputs == 18:
        print("REDDISH-BROWN OF BURNT SIENNA"
              "\nColor code: #E97451")
    elif inputs == 21:
        print("BLUE-VIOLET"
              "\nColor code: #8a2be2")

    # Asking the user for input
    pen = Turtle()
    part_selector = int(input("\nIn which part do you want this color to be filled?"
                              "\n[1] Feet"
                              "\n[2] Hand"
                              "\n[3] Body"
                              "\n[4] Head"
                              "\n[5] Ears"
                              "\nEnter here:"))

    # Using the coordinates again to fill each part
    # Using the color code for better results

    if part_selector == 1:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)
        # The coordinates for the feet of the teddy bear
        pen.penup()
        pen.goto(-155, -190)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=60)
        pen.end_fill()
        # Feet 2
        pen.penup()
        pen.goto(155, -190)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=60)
        pen.end_fill()

        pen.hideturtle()

    elif part_selector == 2:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(100, -50)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=60)
        pen.end_fill()

        pen.penup()
        pen.goto(-100, -50)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=60)
        pen.end_fill()

        pen.hideturtle()

    elif part_selector == 3:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(0, -190)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=150)
        pen.end_fill()

        pen.hideturtle()

    elif part_selector == 4:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(0, 110)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=80)
        pen.end_fill()

        pen.hideturtle()

    elif part_selector == 5:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(100, 195)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=50)
        pen.end_fill()

        pen.penup()
        pen.goto(-100, 195)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=50)
        pen.end_fill()

        pen.hideturtle()

    screen.update()  # Update the turtle screen

    choices = int(input("\nAre all of the shapes filled?"
                        "\nIf yes press '1'"
                        "\nIf not yet press '2'"
                        "\nEnter here:"))

    if choices == 1:
        print("Program Completed.")
        break
    elif choices == 2:
        print("Program Continued")
        continue
