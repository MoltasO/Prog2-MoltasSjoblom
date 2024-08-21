from sys import stdout
from os import get_terminal_size

termSizeX, termSizeY = get_terminal_size().columns,get_terminal_size().lines

def write(textStr: str):
    stdout.write(textStr)

print(termSizeX, termSizeY)

def main():
    pass


if __name__ == "__main__":
    main()