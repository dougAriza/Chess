from turtle import position
from chess.Color import Color
from entities.Piece import Piece
import numpy as np
class King(Piece):
    def __init__(self, color:Color, position:list) -> None:
        super().__init__(color, position)

    def __str__(self) -> str:
        return "King"

    

    def possibleMoves(self)->list:
        moves = np.empty([8,8], dtype=bool)
        moves[:][:] = False
        row = self.getPosition()[0]
        collumn = self.getPosition()[1]

        

        return moves

    