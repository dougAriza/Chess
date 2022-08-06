from entities.Color import Color
from entities.Piece import Piece
class Bishop(Piece):
    def __init__(self, color:Color) -> None:
        super().__init__(color)

    def __str__(self) -> str:
        return "Bishop"
    
    def possibleMoves(self)->None:
        pass