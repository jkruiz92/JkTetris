import os
import turtle
import time
import threading

class tetris():
    def __init__(self):
        print("Starting game...")
        print(os.getcwd())

        self.menu = turtle.Screen()
        self.menu.setup(500, 400)
        self.menu.title("JkTetrisGame     @jkruiz")
        self.menu.bgcolor("black")
        turtle.ht()
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
        print("Playing...")
        self.menu.clear()
        self.menu.setup(350, 500)
        self.menu.title("JkTetrisGame     @jkruiz")
        self.menu.bgcolor("light green")
        turtle.color("light green")
        turtle.setposition(-150, 200)
        turtle.color("black")
        turtle.speed(2)
        turtle.st()

        self.menu.listen()

        self.thread_turtle_down = threading.Thread(target=self.continuous_down)
        self.thread_turtle_down.start()

        self.menu.onkey(self.up, "Up")
        self.menu.onkey(self.down, "Down")
        self.menu.onkey(self.left, "Left")
        self.menu.onkey(self.right, "Right")
        self.menu.onkey(self.close, "space")
                
        self.menu.mainloop()

        

    def close(self):
        print("Closing...")

        self.menu.bye()
        

    def up(self):

        turtle.setheading(90)
        y = turtle.position()[1]
        turtle.sety(y+100)

    def down(self):
        turtle.setheading(-90)
        y = turtle.position()[1]
        turtle.sety(y-100)        

    def left(self):
        turtle.setheading(180)
        turtle.forward(100)

    def right(self):
        turtle.setheading(0)
        turtle.forward(100)

    def continuous_down(self):
        while True:
            self.cont_down=True
            turtle.setheading(-90)
            y = turtle.position()[1]
            turtle.sety(y - 10)
            time.sleep(1)



if __name__ == "__main__":
    tetris()
