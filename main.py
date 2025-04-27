import turtle

screen=turtle.Screen()
pen=turtle.Turtle()
pen.speed(10)
pen.color("Blue")
length = int(input('length of loop: '))
loop = int(input('How many times to loop: '))

numbers = []

for ii in range(length):
  new_number = input("Please input your "+str(ii+1)+" number.")
  numbers.append(int(new_number))

#print(numbers)

def step_any_loop(numbers, repeats):
  n = len(numbers)

  for i in range(repeats):
    for ii in range(n):
      pen.forward(numbers[ii] * 10)
      pen.right(90)

step_any_loop(numbers,length)
#hide turtle 
pen.hideturtle()
turtle.done()
#keep turtle window open when done
#print(turtle.distance(0,0))
print("hello world")

#(1,2,3,4)
#(0+1-3,1-2+4) = (-2,3)

#(0,0), (-2,3)

# distance = sqrt((3-0)^2+(-2-0)^2)

#distance = ((x1-x2)**2+(y1-y2)**2)**0.5

def distance_between_points(point1,point2):
  x1,y1 = point1
  x2,y2 = point2

  distance = ((x2-1)**2+(y2-y1)**2)**0.5

  return distance



p1 = (0,0)
p2 = (2,2)
output = distance_between_points(p1,p2)
print(output)
if output == 0:
  print("closed shape")
else:
  print('not a closed shape')
  