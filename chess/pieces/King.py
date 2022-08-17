from turtle import position
from board.Position import Position
from chess.Color import Color
from chess.Piece import Piece
import numpy as np
class King(Piece):
    def __init__(self, color:Color, position:Position) -> None:
        super().__init__(color, position)

    def __str__(self) -> str:
        return "King"

    def possibleMoves(self)->list:
        moves = np.empty([8,8], dtype=bool)
        moves[:][:] = False
        row = self.getPosition().getRow()
        collumn = self.getPosition().getColumn()
        

        

        return moves

    