import os
import turtle
import time

class tetris():
    def __init__(self):
        print("Starting game...")
        print(os.getcwd())

        self.menu = turtle.Screen()
        self.menu.setup(500, 500)
        self.menu.title("JkTetrisGame     @jkruiz")
        self.menu.bgcolor("black")
        self.menu.listen()
        self.menu.onkey(self.playing, "Up")
        self.menu.mainloop()

    def playing(self):
        self.menu.bye()
        print("Playing...")
        play_screen = turtle.Screen()
        play_screen.setup(350, 500)
        play_screen.bgcolor("green")


if __name__ == "__main__":
    tetris()