from board.Board import Board
from board.Position import Position
from chess.Color import Color
from chess.Piece import Piece
class Knight(Piece):
    def __init__(self, color:Color, position:Position, board:Board) -> None:
        super().__init__(color, position,board)

    def __str__(self) -> str:
        return "Knight"

    def possibleMoves(self)->None:
        pass