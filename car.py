from turtle import Turtle
import random

# ~~~~~~~~~~~~~~~~~~~~ Necessary Constants ~~~~~~~~~~~~~~~~~~~~
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


# ~~~~~~~~~~~~~~~~~~~~ CarManager Class ~~~~~~~~~~~~~~~~~~~~
class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        """A method that creates a car at a random y coordinate."""
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
            new_car.position()
            random_y = random.randint(-240, 270)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def keep_moving(self, player_level):
        """A method that makes all cars move."""
        for each_car in self.all_cars:
            current_speed = STARTING_MOVE_DISTANCE + (STARTING_MOVE_DISTANCE * (player_level-1))
            future_x = each_car.xcor() - current_speed
            each_car.goto(future_x, each_car.ycor())

    def remove_cars(self):
        """A method that removes all the cars."""
        for car in self.all_cars:
            car.ht()
        self.all_cars = []
