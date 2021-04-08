# import turtle
from turtle import *

class WTurtle(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def jumpto(self, x, y):
        self.up()
        self.goto(x, y)
        self.down()


class GridTurtle(WTurtle):
    def __init__(self, width, *args, **kwargs):
        super().__init__('classic', *args, **kwargs)
        self.hideturtle()
        self.color('mistyrose')
        self.grid_width = width
        self.speed(0)
    
    def dashed(self, x, y):
        '''todo'''
        pass
    
    def draw(self, width, height):
        horizontal_line_total = height // self.grid_width + 1
        vertical_line_total = width // self.grid_width + 1
        # original point
        self.dot(10)
        self.jumpto(-width // 2, height // 2)
        # horizontal lines
        for _ in range(horizontal_line_total):
            self.goto(self.xcor() + width, self.ycor())
            self.jumpto(self.xcor() - width, self.ycor() - self.grid_width)
        self.jumpto(-width // 2, height // 2)
        # vertical lines
        for _ in range(vertical_line_total):
            self.goto(self.xcor(), self.ycor() - height)
            self.jumpto(self.xcor() + self.grid_width, self.ycor() + height)

    def axes(self, width, height):
        # arrow
        self.color('orangered')
        self.jumpto(- width // 2 - 30, 0)
        self.setheading(0)
        self.forward(width + 60)
        self.stamp()
        self.jumpto(0, -height // 2 - 30)
        self.setheading(90)
        self.forward(height + 60)
        self.stamp()
    
    def label(self, width, height):
        self.color('slateblue')
        self.up()
        x = -width // 2
        y = height // 2
        self.goto(x, y)
        self.setheading(0)
        for i in range(x, -x + 1, self.grid_width):
            self.write(i, align='center')
            self.forward(self.grid_width)
        self.goto(x, y - 8)
        self.setheading(-90)
        for i in range(y, -y - 1, -self.grid_width):
            self.write(i, align='right')
            self.forward(self.grid_width)
            

    
__grid_turtle = GridTurtle(50)
def show_axes(grid=True, label=True):
    if grid:
        tracer(False)
        __grid_turtle.draw(1000, 800)
        tracer(True)
    __grid_turtle.axes(1000, 800)
    if grid and label:
        __grid_turtle.label(1000, 800)

def hide_axes():
    __grid_turtle.reset()