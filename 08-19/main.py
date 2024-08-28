from sys import stdout
from os import get_terminal_size
from time import sleep
from random import randint
termSizeX, termSizeY = get_terminal_size().columns,get_terminal_size().lines


def write(textStr: str):
    stdout.write(textStr)

print(termSizeX, termSizeY)
class Ball():
    def __init__(self, posX, posY, velX, velY) -> None:
        self.posX = posX
        self.posY = posY
        self.VelX = velX
        self.VelY = velY
        self.Acceleration = 1
        self.Color = randint(30, 37)

balls: list[Ball] = []

def calculateBalls():
    for i in balls:
        i.posX += i.VelX
        i.posY -= i.VelY
        i.VelY -= 1 #Gravity
        if i.posY >= termSizeY:
            i.posY = termSizeY
            i.VelY = -i.VelY
        elif i.posY <= 0:
            i.posY = 0
            i.VelY = -i.VelY
        
        if i.posX <= 0:
            i.posX = 0
            i.VelX = -i.VelX
        elif i.posX >= termSizeX:
            i.posX = termSizeX
            i.VelX = -i.VelX
        

def drawBalls():
    write("\033[2J")
    for i in balls:
        write(f"\033[{i.posY};{i.posX}H")
        write(f"\033[{i.Color}mX")



def main():
    write("\033[?25l")
    for i in range(20):
        newBall = Ball(randint(0,termSizeX), randint(0,termSizeY), randint(0,5), randint(0,5))
        balls.append(newBall)
    while True:
        sleep(0.02)
        calculateBalls()
        drawBalls()

if __name__ == "__main__":
    main()
    write("\033[?25h")
    