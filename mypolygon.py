import turtle
import math

def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

def arc(t, r, angle):
    arc_lenght = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_lenght / 4) + 3
    step_length = arc_lenght / n
    step_angle = float(angle) / n
    t.lt(step_angle / 2)
    for _ in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    t.rt(step_angle / 2)
    
bob = turtle.Turtle()
print(bob)
arc(bob, 100, 180)
circle(bob, 100)
square(bob, 100)
polygon(bob, 100, 6)
turtle.mainloop()