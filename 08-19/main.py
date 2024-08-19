from sys import stdout
from os import get_terminal_size
from time import sleep

termSizeX, termSizeY = get_terminal_size().columns,get_terminal_size().index

def write(textStr: str):
    stdout.write(textStr)

print(termSizeX, termSizeY)
class Ball():
    def __init__(self, posX, posY) -> None:
        self.posX = posX
        self.posY = posY
        self.VelX = 0
        self.VelY = 0
        self.Acceleration = 1
        self.Color = 31
        balls.append(self)

balls: list[Ball]

def calculateBalls():
    for i in balls:
        i.posX += i.VelX
        i.posX += i.VelX
        i.VelY -= 1 #Gravity

def drawBalls():
    write("\033[2J")
    for i in balls:
        write(f"\033[{i.posY};{i.posX}H")
        write(f"\033[{i.Color}m")



def main():
    newBall = Ball()
    while True:
        sleep(1)
        calculateBalls()
        drawBalls()
