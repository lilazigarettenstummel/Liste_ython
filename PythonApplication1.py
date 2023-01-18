from tkinter import *

print("Hello")
name = input("Whats your name? ")
print("Your name is " + name + ".")
question = input("What do u wanna see? ")
if question == ("circle"):
    print("You had chosen " + question + ".")
    from turtle import *

    circle(100)


elif question == ("triangle"):
    print("You had chosen " + question + ".")
    from turtle import *

    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)

elif question == ("square"):
    print("You had chosen " + question + ".")
    from turtle import *

    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

else :
    print("These are the available options:")
    from turtle import *

    circle(100)
    triangle = forward(100), right(120), forward(100), right(120), forward(100)
    square = (
        left(60),
        forward(100),
        left(90),
        forward(100),
        left(90),
        forward(100),
        left(90),
        forward(100),
    )
