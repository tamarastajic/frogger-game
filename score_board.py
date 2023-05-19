from turtle import Turtle

# ~~~~~~~~~~~~~~~~~~~~ Necessary Constant ~~~~~~~~~~~~~~~~~~~~
FONT = ("Courier", 24, "normal")


# ~~~~~~~~~~~~~~~~~~~~ Scoreboard Class ~~~~~~~~~~~~~~~~~~~~
class Scoreboard(Turtle):
    def __init__(self, player_stats):
        super().__init__()
        self.penup()
        self.ht()
        self.write_level(player_stats)

    def draw_safe_zones(self):
        """A method that draws safe zones for the player."""
        self.color("black")
        for i in range(-300, 300, 50):
            self.goto(i, 280)
            self.pendown()
            self.goto(i+25, 280)
            self.penup()
            self.goto(i+50, 280)
        for i in range(-300, 300, 50):
            self.goto(i, -250)
            self.pendown()
            self.goto(i + 25, -250)
            self.penup()
            self.goto(i + 50, 250)

    def write_level(self, player_stats):
        """A method that writes the current level."""
        self.clear()
        self.draw_safe_zones()
        self.goto(-280, 220)
        self.write(f"Level: {player_stats}", move=False, align="Left", font=FONT)

    def game_over(self, player_stats):
        """A method that writes Game Over on top of the screen."""
        self.clear()
        self.write_level(player_stats)
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="Center", font=FONT)




