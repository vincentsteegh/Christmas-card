import turtle
import random

class ChristmasCard:
    def __init__(self):
        # Start screen and turtle
        self.screen = turtle.Screen()
        self.screen.setup(1020, 860)  # Screen size/height
        self.screen.title("Merry Christmas!")
        self.colors = ["skyblue", "lightgreen", "lightpink"]
        self.current_color_index = 0
        self.change_background_color()  # Initialize background color
        self.t = turtle.Turtle()
        self.t.speed(0)  # Draw speed (0 is the fastest)
        self.snowflakes = []  # List for snowflakes

    def draw_star(self, size):
        # Draw a star of a specific size
        self.t.color("yellow")
        self.t.begin_fill()
        for _ in range(5):
            self.t.forward(size)
            self.t.right(144)
        self.t.end_fill()

    def draw_tree(self, size):
        # Draw a tree of a certain size
        self.t.color("forest green")
        self.t.begin_fill()
        for _ in range(3):
            self.t.forward(size)
            self.t.left(120)
        self.t.end_fill()

    def draw_ornament(self, size):
        # Draw a circle ornament of a certain size
        colors = ["red", "blue", "yellow", "purple", "orange"]
        self.t.color(random.choice(colors))
        self.t.begin_fill()
        self.t.circle(size)
        self.t.end_fill()

    def draw_ground(self):
        # Draw the snow from the ground
        self.t.penup()
        self.t.goto(-520, -200)
        self.t.pendown()
        self.t.color("white")
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(1200)
            self.t.right(90)
            self.t.forward(200)
            self.t.right(90)
        self.t.end_fill()

    def draw_race_track(self):
        # Draw the race track (yes this idea is related to mario cart)
        self.t.penup()
        self.t.goto(-400, -300)
        self.t.pendown()
        self.t.color("gray")
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(800)
            self.t.left(90)
            self.t.forward(600)
            self.t.left(90)
        self.t.end_fill()

        # Draw the inner track (yes this idea is related to mario cart)
        self.t.penup()
        self.t.goto(-350, -250)
        self.t.pendown()
        self.t.color("white")
        self.t.width(5)
        for _ in range(2):
            self.t.forward(700)
            self.t.left(90)
            self.t.forward(500)
            self.t.left(90)
        self.t.width(1)

    def draw_present(self, width, height):
        # Draw a present of a certain width and height
        self.t.color("red")
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(width)
            self.t.left(90)
            self.t.forward(height)
            self.t.left(90)
        self.t.end_fill()
        self.t.color("green")
        self.t.width(3)
        self.t.forward(width / 2)
        self.t.left(90)
        self.t.forward(height)
        self.t.backward(height / 2)
        self.t.left(90)
        self.t.forward(width / 2)
        self.t.backward(width)
        self.t.width(1)

    def place_presents(self):
        y = -180  # Set a fixed y-coordinate for all presents
        positions = [(-300, y), (-150, y), (0, y), (150, y), (300, y)]

        for x, y in positions:
            self.t.penup()
            self.t.goto(x, y)
            self.t.pendown()
            self.draw_present(40, 30)

    def create_snowflake(self):
        # Make a snowflake and place it in the list
        snowflake = turtle.Turtle()
        snowflake.shape("circle")
        snowflake.color("white")
        snowflake.penup()
        snowflake.speed(1)
        snowflake.shapesize(random.uniform(0.5, 1.5))  # Make snowflakes smaller and wider
        snowflake.goto(random.randint(-510, 510), 430)
        self.snowflakes.append(snowflake)

    def move_snowflakes(self):
        # Move snowflakes and reset their position after falling off the screen
        for snowflake in self.snowflakes:
            x, y = snowflake.position()
            snowflake.goto(x + random.randint(-2, 2), y - random.randint(1, 3))
            if y < -300:
                snowflake.goto(random.randint(-510, 510), 430)

    def change_background_color(self):
        # Change the background color in a rotating way
        self.screen.bgcolor(self.colors[self.current_color_index])
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        self.screen.ontimer(self.change_background_color, 1000)  # Change color every second

    def create_card(self):
        # Draw the race track
        self.draw_race_track()

        # Make the Christmas card background
        self.draw_ground()

        # Draw the tree
        tree_sizes = [200, 140, 100]
        y_positions = [-200, -120, -40]
        for size, y in zip(tree_sizes, y_positions):
            self.t.penup()
            self.t.goto(-size/2, y)
            self.t.pendown()
            self.draw_tree(size)

        # This makes the star and places it on top of the tree
        self.t.penup()
        self.t.goto(-30, 65)
        self.t.pendown()
        self.draw_star(60)

        # Draw ornaments
        ornament_count = 0
        while ornament_count < 15:
            # Generate coordinates for ornaments inside the tree
            x = random.uniform(-50, 50)
            y = random.uniform(-200, 100)

            # Control where ornaments are placed
            in_tree = any(
                base_y <= y <= base_y + size * (3 ** 0.5) / 2 and abs(x) <= (y - base_y) / (3 ** 0.5)
                for size, base_y in zip(tree_sizes, y_positions)
            )

            if in_tree:
                self.t.penup()
                self.t.goto(x, y)
                self.t.pendown()
                self.draw_ornament(5)
                ornament_count += 1

        # Place presents inside the circuit
        self.place_presents()

        # Text
        self.t.penup()
        self.t.goto(0, -325)
        self.t.color("red")
        try:
            self.t.write("Merry Christmas!", align="center", font=("Arial", 40, "bold"))
        except turtle.TurtleGraphicsError:
            print("Error: Unable to write text. Check your font settings.")

        self.t.hideturtle()

        # Make snowflakes
        for _ in range(50):
            self.create_snowflake()

    def animate(self):
        # Move snowflakes
        while True:
            self.move_snowflakes()
            self.screen.update()

    def run(self):
        # Self start
        self.screen.tracer(0)  # Turn off animation
        self.create_card()
        self.screen.ontimer(self.animate, 50)
        self.screen.mainloop()

# Start the card
card = ChristmasCard()
card.run()