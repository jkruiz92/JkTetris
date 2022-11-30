import os
import turtle
import time

class tetris():
    def __init__(self):
        print("Starting game...")
        print(os.getcwd())

        self.menu = turtle.Screen()
        self.menu.setup(500, 400)
        self.menu.title("JkTetrisGame     @jkruiz")
        self.menu.bgcolor("black")
        turtle.hideturtle()
        turtle.penup()
        turtle.setposition(-150, 100)
        turtle.color("green")
        turtle.write("Start Play!", move=False, font=("Verdana", 20, "normal"),  align="left")
        turtle.setposition(-150, 50)
        turtle.write("Close", move=False, font=("Verdana", 20, "normal"),  align="left")
        self.menu.listen()
        self.menu.onkey(self.playing, "Up")
        self.menu.onkey(self.close, "Down")
        self.menu.mainloop()

    def playing(self):
        self.menu.bye()
        print("Playing...")
        play_screen = turtle.Screen()
        play_screen.setup(350, 500)
        play_screen.bgcolor("light green")

    def close(self):
        self.menu.bye()


if __name__ == "__main__":
    tetris()
