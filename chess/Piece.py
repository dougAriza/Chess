from abc import ABC, abstractmethod
from board.Position import Position
from chess.Color import Color

class Piece(ABC):
    def __init__(self, color:Color, position:Position) -> None:
        self.count:int = 0
        self.selectPiece:bool = False
        self.color:str = color
        self.position = position

    def __str__(self) -> str:
        return "Piece"
        
    @abstractmethod
    def possibleMoves(self)->None:
        pass

    def specialMoves(self)->None:
        pass

    def move(self, origin:str)->str:
        destiny = ""
        self.count += 1
        return destiny

    def setPosition(self, position:Position)->None:
        self.position = position

    def getPosition(self)->Position:
        return self.position

    def setColor(self, color:str)->None:
        self.color = color

    def getColor(self)->str:
        return self.color

    def getCount(self)->int:
        return self.position

    def setSelectPiece(self, state:bool)->None:
        self.selectPiece = state

    def getSelectPiece(self)->bool:
        return self.selectPiece