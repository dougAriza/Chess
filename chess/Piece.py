from abc import ABC, abstractmethod
from board.Position import Position

from chess.Color import Color
class Piece(ABC):
    def __init__(self, color:Color, position:Position) -> None:
        self.__count:int = 0
        self.__selectPiece:bool = False
        self.__color:str = color
        self.__position = position

    def __str__(self) -> str:
        return "Piece"
        
    @abstractmethod
    def possibleMoves(self)->None:
        pass

    def specialMoves(self)->None:
        pass

    def move(self, origin:str)->str:
        destiny = ""
        self.__count += 1
        return destiny

    def setPosition(self, position:Position)->None:
        self.__position = position

    def getPosition(self)->Position:
        return self.__position

    def setColor(self, color:str)->None:
        self.__color = color

    def getColor(self)->str:
        return self.__color

    def getCount(self)->int:
        return self.__position

    def setSelectPiece(self, state:bool)->None:
        self.__selectPiece = state

    def getSelectPiece(self)->bool:
        return self.__selectPiece