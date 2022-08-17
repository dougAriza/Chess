
class Position():
    def __init__(self, row:int, column:int) -> None:
        self.__row = row
        self.__column = column

    def setRow(self, row:int):
        self.__row = row

    def getRow(self)-> int:
        return self.__row

    def setColumn(self, column:int):
        self.__column = column

    def getColumn(self)->int:
        return self.__column

    def convertChessPosition(self)->str:
        chessPosition:str
        if self.__column == 0:
            chessPosition = "A"
        elif self.__column == 1:
            chessPosition = "B"
        elif self.__column == 2:
            chessPosition = "C"
        elif self.__column == 3:
            chessPosition = "D"
        elif self.__column == 4:
            chessPosition = "E"
        elif self.__column == 5:
            chessPosition = "F"
        elif self.__column == 6:
            chessPosition = "G"
        elif self.__column == 7:
            chessPosition = "H"

        chessPosition += str(8 - self.__row)
        return chessPosition