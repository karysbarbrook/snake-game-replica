from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        # creates initial snake for start of game, 3 segments as seen in START_POSITIONS
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # creates 1 new segment
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake_segments.append(new_snake)

    def extend_snake(self):
        # add new segment to end of snake every time food is collected (specifically, same coordinates as last segment)
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(RIGHT)
