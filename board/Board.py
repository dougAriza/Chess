import numpy as np
from board.Position import Position
from chess.Piece import Piece


class Board:
    def __init__(self) -> None:
        self.__positions = np.empty([8,8], dtype=Piece)

    def __str__(self) -> str:
        strBoard = ""
        for i in range(8):
            s=""
            for j in range(8):
                s += self.__positions[i,j].__str__() + " "
            strBoard += s + "\n"
        return strBoard

    def isTherePiece(self, position:str)->Piece:
        row = 8 - int(position[1])
        column = (ord(position[0]) - 65)
        return self.__positions[row,column]

    def getPositions(self)-> np:
        return self.__positions

    def putPiece(self, piece:Piece, position:Position):
        chessPosition = position.convertChessPosition()
        if self.isTherePiece(chessPosition) == None:
            self.__positions[position.getRow(), position.getColumn()] = piece

    def isTherePosition(self, position:Position)-> bool:
        if (position.getRow() < 0) or (position.getRow() > 7 ) or (position.getColumn() < 0) or (position.getColumn() > 7):
            return True
        return False
