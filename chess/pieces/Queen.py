from chess.Color import Color
from entities.Piece import Piece
class Queen(Piece):
    def __init__(self, color:Color) -> None:
        super().__init__(color)

    def __str__(self) -> str:
        return "Queen"

    def possibleMoves(self)->None:
        pass