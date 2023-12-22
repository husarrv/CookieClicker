from operator import inv
from time import sleep
# import typer
# import cv2
import tkinter as tk
import time
# from pynput.mouse import Listener
import turtle

clicks = 0
level = 1

# app = typer.Typer()

# @app.command()
def clicker():

    wnd = turtle.Screen()
    wnd.title("Cookie Clicker")
    wnd.bgcolor("black")


    wnd.register_shape("cookie.gif")

    cookie = turtle.Turtle()

    cookie.shape("cookie.gif")
    cookie.speed(0)

    def levelUp(x, y):
        global level
        global clicks
        
        if clicks >= 20 and level == 1:
            level += 1
            clicks -= clicks
            pen.clear()
            pen.write(f"Clicks:{clicks}", align = "center", font = ("Courier New",32,"normal"))

        if clicks >= 40 and level == 2:
            level += 1
            clicks -= clicks
            pen.clear()
            pen.write(f"Clicks:{clicks}", align = "center", font = ("Courier New",32,"normal"))

        if clicks >= 60 and level == 3:
            level += 1
            clicks -= clicks
            pen.clear()
            pen.write(f"Clicks:{clicks}", align = "center", font = ("Courier New",32,"normal"))

        if clicks >= 80 and level == 4:
            level += 1
            clicks -= clicks
            pen.clear()
            pen.write(f"Clicks:{clicks}", align = "center", font = ("Courier New",32,"normal"))

        button.clear()
        button.write(f"Level up! Actually lvl -> {level}", align='center', font=("Courier New",21,"bold"))

    button = turtle.Turtle()
    button.hideturtle()
    # button.shape('square')
    button.color('white')
    # button.fillcolor("white")
    button.penup()
    # button.shapesize()
    button.goto(0,250)
    button.write(f"Level up! Actually lvl -> {level}", align='center', font=("Courier New",21,"bold"))
    button.onclick(levelUp)
    button.showturtle()
    



    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("white")
    pen.penup()
    pen.goto(0,300)
    pen.write(f"Clicks:{clicks}", align = "center", font = ("Courier New",32,"normal"))


    def clicked(x, y):
        global clicks
        global level

        if level==1:
            clicks += 1
        if level==2:
            clicks += 2
        if level==3:
            clicks += 3
        if level==4:
            clicks += 4
        if level==5:
            clicks += 5
        pen.clear()
        pen.write(f"Clicks:{clicks}", align = "center", font = ("Courier New",32,"normal"))

    
    cookie.onclick(clicked)

    wnd.mainloop()


if __name__ == "__main__":
    clicker()
