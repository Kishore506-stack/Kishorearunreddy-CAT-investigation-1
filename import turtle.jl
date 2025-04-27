import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the speed (0 is fastest, 1 is slowest)
dist = distance(50, 50)
angle = towards(50, 50)
# Set the color of the turtle
my_turtle.color("blue")

# Set the fill color (optional)
my_turtle.fillcolor("cyan")  # Example: Fill with cyan

# Start filling the shape (optional)
my_turtle.begin_fill()

# Draw a square
for _ in range(4):  # Repeat the following 4 times
    my_turtle.forward(100)  # Move forward 100 units
    my_turtle.left(90)     # Turn left by 90 degrees

# Stop filling the shape (optional)
my_turtle.end_fill()

# Hide the turtle (optional)
my_turtle.hideturtle()

# Keep the window open until it's closed manually
turtle.done()