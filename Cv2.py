import math
import turtle
from random import random

"""""
if maxFloor <= 10: ratio = 50
if 10 < maxFloor <= 50: ratio = 10
if 50 < maxFloor <= 100: ratio = 5
if 100 < maxFloor <= 150: ratio = 3
if 150 < maxFloor <= 200: ratio = 2
"""


def Elevator_Traffic_Simulator(elevList, callList, maxFloor):
    turtle.Turtle()
    turtle.color("red")
    turtle.penup()
    turtle.goto(0, -120)

    ratio = 400/maxFloor
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Elevator Traffic Simulator")

    elevSimulate = turtle.Turtle()
    elevSimulate.shape("square")
    elevSimulate.penup()

    elevIndexCalls = [len(elevList)]
    for e in elevList:
        listOfCalls = []
        for call in callList:
            if call._elevIndex == e._index:
                listOfCalls.append(call)
        elevIndexCalls.append(listOfCalls)

    i = -1
    for list in elevIndexCalls:
        i += 1
        speed = math.ceil(elevList[i]._speed)
        elevSimulate.speed(speed)
        R = random()
        B = random()
        G = random()
        elevSimulate.color(R, G, B)
        for call in listOfCalls:
            src = int(call._src)
            dest = int(call._dest)
            elevSimulate.goto(0, ((src * ratio) - 120))
            elevSimulate.goto(0, ((dest * ratio) - 120))
