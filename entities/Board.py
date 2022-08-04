import numpy as np


import numpy as np
from entities.Piece import Piece
from entities.pieces import Bishop, King, Knight, Pawn, Queen, Rook

class Board:
    def __init__(self) -> None:
        self.__pieces:np
        self.position = self.__generateBoard()

    def __generateBoard(self)->np:
        board = []
        for i in range(8):
            collumn = []
            for j in range(8):
                collumn.append("x")
            board.append(collumn)
        return board
    