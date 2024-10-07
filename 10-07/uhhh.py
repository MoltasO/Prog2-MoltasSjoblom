
class matrix():
    def __init__(self, sizex, sizey, prefabMetrix: list[list[int]] = None) -> None:
        self.y: int = sizey
        self.x: int = sizex

        self.matrix: list[list[int]] = []
        if prefabMetrix == None:
            for i in range(sizey):
                newList = list()
                self.matrix.append(newList)
                for j in range(sizex):
                    newList.append(0)
        else:
            self.matrix = prefabMetrix.copy()

    def __getitem__(self, value: tuple[int]):
        print(value[0], value[1])
        if (self.x-1 >= value[0] >= 0) and (self.y-1 >= value[1] >= 0):
            return self.matrix[(value[0])][value[1]]
        raise TypeError(f"Trying to index outside of matrix {value}")
    
    def __setitem__(self, value: object, newvalue: int|float):
        if not (isinstance(newvalue, int) or isinstance(newvalue, float)):
            raise TypeError("Cannot use any other type other than numbers (int/float)")
        if (self.x >= value[0] >= 0) and (self.y >= value[1] >= 0):
            self.matrix[(value[0])][value[1]] = newvalue
        else:
            raise TypeError(f"Trying to index outside of matrix {value}")
    
    def __mul__(self, other: object):
        
        if isinstance(other, matrix):
            if self.y != other.x:
                raise TypeError("Matrix multiplication is not defined bwtween matrixes of these sizes.")
            tempMatrix = matrix(self.x, other.y)
            for i in range(tempMatrix.y):
                for j in range(tempMatrix.x):
                    tempNum = 0
                    for n in range(self.y):
                        tempNum += self[i,n]*other[n,j]
                        tempMatrix[i,j] = tempNum
            return tempMatrix
        elif (isinstance(other, int) or isinstance(other, float)):
            tempMatrix = matrix(self.x, self.y)
            for i in range(self.y):
                for j in range(self.x):
                    tempMatrix[j,i] = self[j,i]*other
            return tempMatrix
        else:
            raise TypeError("Must multiply a matrix by a valid object")
        
    
    def __str__(self) -> str:
        _buffer: str = ""
        for i in self.matrix:
            _buffer += '|'
            for j in i:
                _buffer += f" {j}"
            _buffer += ' |\n'
        return _buffer

    def __add__(self, value: object):
        tempMatrix = matrix(self.x, self.y)
        if isinstance(value, matrix):
            if not ((value.x == self.x) and (value.y == self.y)):
                raise TypeError("Can not add matrixes of diffrend sizes")
            for i in range(self.y):
                for j in range(self.x):
                    tempMatrix[i, j] = self[i, j] + value[i, j]
            return tempMatrix
        elif (isinstance(value, int) or isinstance(value, float)):
            for i in range(self.y):
                for j in range(self.x):
                    tempMatrix[i, j] = self[i, j] + value
            return tempMatrix
        raise TypeError("Can not add other types other than int and matrix")
    
    def __sub__(self, value: object):            
        if (isinstance(value, int) or isinstance(value, float)):
            return self.__add__(-value)
        
        elif isinstance(value, matrix):
            tempMatrix = matrix(self.x, self.y)
            if not ((value.x == self.x) and (value.y == self.y)):
                raise TypeError("Can not add matrixes of diffrend sizes")
            for i in range(self.y):
                for j in range(self.x):
                    tempMatrix[i, j] = self[i, j] - value[i, j]


    def __eq__(self, value: object | int | float) -> bool:
        if (isinstance(value, float) or isinstance(value, int)):
            for i in self.matrix:
                for j in i:
                    if j != value:
                        return False
            return True
        if not isinstance(value, matrix):
            return False
        if self.matrix != value.matrix:
            return False
        return True

    def getLargestPos(self) -> tuple[int ,int]:
        largestPos: tuple = None
        largest: int = 0
        for i in range(self.y):
            for j in range(self.x):
                if self[j,i] > largest:
                    largest = self[j,i]
                    largestPos = (i+1,j+1)
        return largestPos
   

newMatrix = matrix(1,4,[[5],[5],[5],[5]])
otherMatrix = matrix(4,2,[[1,1,3,4],[10,6,9,8]])

#print(newMatrix.getLargestPos())
print(newMatrix == 5)

print(newMatrix*otherMatrix)
