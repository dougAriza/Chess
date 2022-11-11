from board.Board import Board
from board.Position import Position
from chess.Color import Color
from chess.Piece import Piece
import numpy as np
class King(Piece):
    def __init__(self, color:Color, position:Position, board:Board) -> None:
        super().__init__(color, position)
        self.__board = board

    def __str__(self) -> str:
        return "King"

    def possibleMoves(self)->list:
        moves = np.empty([8,8], dtype=bool)
        moves[:][:] = False
        row = self.getPosition().getRow()
        column = self.getPosition().getColumn()
        
        p = Position(row, column)
        if (self.__board.isTherePiece(p.convertChessPosition()) != None) and (self.__board.isTherePosition(p) == False):
            moves[p.getRow(),p.getColumn()] = True
        
        return moves

    