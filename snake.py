
from turtle import Turtle
START_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in START_POSITION:
          self.add_segment(position)
    def add_segment(self,position):

        snake_1 = Turtle(shape="square")
        snake_1.color("white")
        snake_1.penup()
        snake_1.goto(position)
        self.segments.append(snake_1)

    def extend(self):
        self.add_segment(self.segments[-1].position()) #position() is a method comes from turtle
        # class

    def Move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
