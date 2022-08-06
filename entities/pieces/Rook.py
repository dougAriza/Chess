from entities.Color import Color
from entities.Piece import Piece
class Rook(Piece):
    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def __str__(self) -> str:
        return "Rook"

    def possibleMoves(self)->None:
        pass