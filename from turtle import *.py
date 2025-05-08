import turtle
screen=turtle.Screen()
pen=turtle.Turtle()
pen.speed(10)
length = int(input('length of loop: '))

numbers = []

for ii in range(length):
  new_number = input("Please input your "+str(ii+1)+" number.")
  numbers.append(new_number)

#print(numbers)

def step_any_loop(numbers, repeats):
#draw line

 n = len(numbers)

 for i in range(repeats):
    for i in range(n):
      pen.forward(numbers[i] * 100)
      pen.right(90)
step_any_loop( [3, 1, 2, 1], 4)
#hide turtle 
pen.hideturtle()
turtle.done()
#keep turtle window open when done