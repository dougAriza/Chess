from abc import ABC, abstractmethod
class Piece(ABC):
    def __init__(self) -> None:
        self.__position:str
        self.__count:int
        self.__selectPiece:bool
        
    @abstractmethod
    def possibleMoves(self)->None:
        pass

    def specialMoves(self)->None:
        pass

    def move(self, origin:str)->str:
        destiny = ""
        self.__count += 1
        return destiny

    def setPosition(self, position:str)->None:
        self.__position = position

    def getPosition(self)->str:
        return self.__position

    def getCount(self)->int:
        return self.__position

    def setSelectPiece(self, state:bool)->None:
        self.__selectPiece = state

    def getSelectPiece(self)->bool:
        return self.__selectPiece