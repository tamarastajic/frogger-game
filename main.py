import time
from turtle import Screen
from player import Player
from car import CarManager
from score_board import Scoreboard


# ~~~~~~~~~~~~~~~~~~~~ Necessary Functions ~~~~~~~~~~~~~~~~~~~~
def key_binds():
    """A function that listens for specific key presses."""
    global screen
    screen.listen()
    screen.onkey(key="Up", fun=player.move_up)
    screen.onkey(key="Left", fun=player.move_left)
    screen.onkey(key="Right", fun=player.move_right)


def change_level(level):
    """A function that changes the current level to the next one."""
    player.reset_pos()
    car_manager.remove_cars()
    player.level = level
    score.write_level(player.level)
    screen.update()
    key_binds()


# ~~~~~~~~~~~~~~~~~~~~ Creating the Game Screen ~~~~~~~~~~~~~~~~~~~~
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger!")
screen.tracer(0)

# ~~~~~~~~~~~~~~~~~~~~ Creating Necessary Objects ~~~~~~~~~~~~~~~~~~~~
player = Player()
car_manager = CarManager()
score = Scoreboard(player.level)

# ~~~~~~~~~~~~~~~~~~~~ Listening to key presses ~~~~~~~~~~~~~~~~~~~~
key_binds()

# ~~~~~~~~~~~~~~~~~~~~ Game Loop ~~~~~~~~~~~~~~~~~~~~
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating cars and making them move.
    car_manager.create_car()
    car_manager.keep_moving(player.level)

    # Removing cars out of bounds.
    for each_car in car_manager.all_cars:
        if each_car.xcor() < -320:
            each_car.ht()
            car_manager.all_cars.remove(each_car)

    # Checking if Frogger collided with any car.
    if player.check_collision(car_manager.all_cars):
        score.game_over(player.level)
        if screen.textinput("You lost.", "Do you want to play again? Yes or no.").lower() == "yes":
            change_level(1)
        else:
            game_is_on = False

    # Checking if Frogger went to the next level:
    if player.check_if_won():
        change_level(player.level + 1)
        continue

screen.exitonclick()
