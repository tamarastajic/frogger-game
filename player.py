from turtle import Turtle

# ~~~~~~~~~~~~~~~~~~~~ Necessary Constants ~~~~~~~~~~~~~~~~~~~~
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# ~~~~~~~~~~~~~~~~~~~~ Player Class ~~~~~~~~~~~~~~~~~~~~
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.reset_pos()
        self.setheading(90)
        self.level = 1

    def move_up(self):
        """A method that moves the player up."""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_left(self):
        """A method that moves the player left."""
        if self.xcor() > -290:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x,self.ycor())

    def move_right(self):
        """A method that moves the player right."""
        if self.xcor() < 280:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def check_if_won(self):
        """A method that checks if the player crossed the finish line."""
        return self.ycor() >= FINISH_LINE_Y

    def reset_pos(self):
        """A method that resets the position to the starting one."""
        self.goto(STARTING_POSITION)

    def check_collision(self, cars):
        """A method that checks if player collided with any of the cars."""
        for each_car in cars:
            if each_car.distance(self) < 22:
                return True
        return False

