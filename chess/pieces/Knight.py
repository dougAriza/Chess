from chess.Color import Color
from entities.Piece import Piece
class Knight(Piece):
    def __init__(self, color:Color) -> None:
        super().__init__(color)

    def __str__(self) -> str:
        return "Knight"

    def possibleMoves(self)->None:
        pass