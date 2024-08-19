from sys import stdout
from os import get_terminal_size
from time import sleep

termSizeX, termSizeY = get_terminal_size().columns,get_terminal_size().index

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

def drawFrame():
    sleep(0.1)
    for i in balls:
        i.posX += i.VelX
        i.posX += i.VelX

def main():
    newBall = Ball()
    while True:
        drawFrame()