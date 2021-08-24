from turtle import *

pensize(2)
speed(0)

def go(xx, yy):
    goto(x, y)
    pendown()

def coordinates():
    penup()
    goto(0, -400)
    pendown()
    for i in range(80):
        step = -400 + 10 * i
        # goto(0, step)
        # goto(5, step)
        # goto(-5, step)
        # goto(0, step)
        goto(0, step)
        if (i%5 == 0):
            goto(10, step)
            goto(-10, step)
            goto(0, step)
        if (i%10 == 0):
            goto(20, step)
            goto(-20, step)
            goto(0, step)

    penup()
    goto(-400, 0)
    pendown()
    for i in range(80):
        step = -400 + 10 * i
        # goto(step, 0)
        # goto(step, 5)
        # goto(step, -5)
        # goto(step, 0)
        goto(step, 0)
        if (i%5 == 0):
            goto(step, 10)
            goto(step, -10)
            goto(step, 0)
        if (i%10 == 0):
            goto(step, 20)
            goto(step, -20)
            goto(step, 0)
    penup()

x = []
y = []

# funk = input("Введите формулу (например: у=2x+4)")
funk = "у=2x+4"
second = funk.split("+")
b = int(second[1])
first = second[0].split("=")
k = int(first[1].replace("x", ""))
coordinates()

for x in range(401):
    x = x - 200
    y = (k * x + b)
    go(x,y)

exitonclick()