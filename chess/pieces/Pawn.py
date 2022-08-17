from board.Position import Position
from chess.Color import Color
from chess.Piece import Piece
class Pawn(Piece):
    def __init__(self, color:Color, position:Position) -> None:
        super().__init__(color, position)

    def __str__(self) -> str:
        return "Pawn"

    def possibleMoves(self)->None:
        pass