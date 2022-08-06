from entities.Color import Color
from entities.Piece import Piece
class Pawn(Piece):
    def __init__(self, color:Color) -> None:
        super().__init__(color)

    def __str__(self) -> str:
        return "Pawn"

    def possibleMoves(self)->None:
        pass