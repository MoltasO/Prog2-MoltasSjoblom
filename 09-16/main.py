class myClass:
    __yes = "Yes2"
    words = []
    @staticmethod
    def printwords():
        for i in myClass.words:
            print(i.__num)
        print(myClass.__yes)
    def __init__(self, name: str, number: int) -> None:
        self.__name = name
        self.__num = number
        myClass.words.append(self)
    def printName(self):
        print(self.__name)



def myfunc(*args, **kwargs):
    for i in kwargs.keys(): #values()
        print(i)
    for i in args:
        print(i)


def main():
    obj1 = myClass("Yes", 10)
    obj1.printName()
    myClass.printwords()
    myfunc(1,2,3,4, huh = "nuhu")



if __name__ == "__main__":
    main()