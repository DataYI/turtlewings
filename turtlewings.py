# import turtle
from turtle import *

screen = getscreen()

class WTurtle(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def jumpto(self, x, y):
        self.up()
        self.goto(x, y)
        self.down()


class CoordTurtle(WTurtle):
    def __init__(self, win_width, win_height, grid_width, *args, **kwargs):
        super().__init__('classic', *args, **kwargs)
        self.hideturtle()
        self.color('mistyrose')
        self.win_width = win_width
        self.win_height = win_height
        self.grid_width = grid_width
        self.speed(0)
    
    def dashed(self, x, y):
        '''todo'''
        pass
    
    def grid(self):
        width, height = self.win_width, self.win_height
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

    def axes(self):
        width, height = self.win_width, self.win_height
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
    
    def label(self):
        width, height = self.win_width, self.win_height
        self.color('slateblue')
        self.up()
        x = -width // 2
        y = -height // 2
        # x-axis
        self.goto(x, y - 20)
        self.setheading(0)
        for i in range(x, -x + 1, self.grid_width):
            self.write(i, align='center')
            self.forward(self.grid_width)
        # y-axis
        self.goto(x, y - 8)
        self.setheading(90)
        for i in range(y, -y + 1, self.grid_width):
            self.write(i, align='right')
            self.forward(self.grid_width)
            
    def show_coord(self, x, y):
        width, height = self.win_width, self.win_height
        for _ in range(5):
            self.undo()
        self.color('deeppink')
        self.jumpto(x, y)
        self.dot(5)
        self.jumpto(-width // 2, height // 2 + 10)
        self.write(f'coord: {x:0.0f},{y:0.0f}',font=(None, 20, 'bold'))


class Wings:
    def __init__(self) -> None:
        self.__coord_turtle = CoordTurtle(1000, 800, 50)
    
    def show_axes(self, grid=True, label=True):
        if grid:
            tracer(False)
            self.__coord_turtle.grid()
            tracer(True)
        self.__coord_turtle.axes()
        if grid and label:
            self.__coord_turtle.label()
        
    def hide_axes(self):
        self.__coord_turtle.reset()


    def show_coord_on_click(self):
        for _ in range(5):
            self.__coord_turtle.jumpto(0, 0)
        self.__coord_turtle.show_coord(0, 0)
        onscreenclick(self.__coord_turtle.show_coord)
    
    def using(self):
        self.show_axes()
        self.show_coord_on_click()
    

wings = Wings()