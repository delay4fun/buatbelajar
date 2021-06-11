# # make a square
# Clever Programmer (qazi)

import turtle
from time import sleep

testSquare = turtle.Turtle()
val1 = [0]
val2 = 0

def square(): 
    testSquare.forward(100)
    testSquare.right(90)
    testSquare.forward(100)
    testSquare.right(90)
    testSquare.forward(100)
    testSquare.right(90)
    testSquare.left(100) # comment this line and uncomment below
    # testSquare.forward(100)
# square()
for i in val1:
    val2 += 1
    val1.append(val2)
    print(square())
    sleep(0.1)
