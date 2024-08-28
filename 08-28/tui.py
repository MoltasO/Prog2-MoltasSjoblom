import sys, os
from time import sleep
from rainbowize import Styling

class TEnum:
    textCenterAlign = "center"
    textRightAlign = "right"
    textLeftAlign = "left"

def goto(posx: int, posy: int) -> None:
    sys.stdout.write(f"\033[{posy};{posx}H")

def write(string: str) -> None:
    sys.stdout.write(string)

def clearScr() -> None:
    sys.stdout.flush()
    sys.stdout.write("\033[2J")

def drawFrame(sizex: int, sizey: int, posx: int, posy: int, borderStyleTuple: tuple[str], frameColor: str = None):
    for i in range(sizey):
        goto(posx,posy+i)
        write(borderStyleTuple[0])
        goto(posx+sizex-1,posy+i)
        write(borderStyleTuple[1])
    goto(posx+1,posy)
    write(borderStyleTuple[2]*(sizex-2))
    goto(posx+1,posy+sizey-1)
    write(borderStyleTuple[3]*(sizex-2))


class TMainRoot(): pass

class TWindowType():
    def __init__(self, root: TMainRoot, sizex: int, sizey: int, posx: int, posy: int, bgcolor: tuple = None, fgcolor: tuple = None) -> None:
        self.root = root
        self.sizex = sizex
        self.sizey = sizey
        self.posx = posx
        self.posy = posy
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        root.chidren.append(self)

class TLabel(TWindowType):
    def __init__(self, root: TMainRoot, sizex: int, sizey: int, posx: int, posy: int, textAlign: str = TEnum.textCenterAlign, text:str = "Label", bgcolor: str = None, fgcolor: str = None) -> None:
        super().__init__(root, sizex, sizey, posx, posy, bgcolor, fgcolor)
        self.textAlign = textAlign
        self.text = text

    def draw(self, borderStyleTuple: tuple[str]):
        if self.bgcolor:
            pass
        if self.fgcolor:
            pass
        drawFrame(self.sizex, self.sizey, self.posx, self.posy, borderStyleTuple)
        goto(self.posx+(self.sizex//2-(len(self.text)//2)),self.posy+(self.sizey//2))
        write(self.text)



class TMainRoot():
    def __init__(self, borderStyleTuple: tuple[str] = ("█", "█", "▀", "▄")) -> None:
        self.chidren: list[TWindowType] = []
        self.borderStyleTuple = borderStyleTuple

    def MainLoop(self):
        while True:
            sleep(1)
            clearScr()
            for child in self.chidren:
                child.draw(self.borderStyleTuple)
    
    def DoMainLoopStep(self, movecurs=False):
        clearScr()
        for child in self.chidren:
            child.draw(self.borderStyleTuple)
        if movecurs:
            goto(1,1)

if __name__ == "__main__":
    clearScr()
    Root = TMainRoot()
    newLabel = TLabel(Root, 30,10,10,10, text="Hello")
    ptherLabel = TLabel(Root, 30,10,50,10, text="Amogus ඞ")
    #newLabel.posx += 1
    Root.DoMainLoopStep(movecurs=True)