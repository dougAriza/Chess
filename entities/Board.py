import numpy as np
from entities.Color import Color
from entities.Piece import Piece
from entities.pieces import Bishop, King, Knight, Pawn, Queen, Rook

class Board:
    def __init__(self) -> None:
        self.__positions = np.empty([8,8], dtype=Piece)
        self.__generateBoard()

    def __str__(self) -> str:
        strBoard = ""
        for i in range(8):
            s=""
            for j in range(8):
                s += self.__positions[i,j].__str__() + " "
            strBoard += s + "\n"
        return strBoard

    def __generateBoard(self)->np:
        self.__positions[0,0] = Rook.Rook(Color.BLACK)
        self.__positions[0,1] = Knight.Knight(Color.BLACK)
        self.__positions[0,2] = Bishop.Bishop(Color.BLACK)
        self.__positions[0,3] = Queen.Queen(Color.BLACK)
        self.__positions[0,4] = King.King(Color.BLACK)
        self.__positions[0,5] = Bishop.Bishop(Color.BLACK)
        self.__positions[0,6] = Knight.Knight(Color.BLACK)
        self.__positions[0,7] = Rook.Rook(Color.BLACK)
        for x in range(8):
            self.__positions[1,x] = Pawn.Pawn(Color.BLACK)

        self.__positions[7,0] = Rook.Rook(Color.WHITE)
        self.__positions[7,1] =  Knight.Knight(Color.WHITE)
        self.__positions[7,2] =  Bishop.Bishop(Color.WHITE)
        self.__positions[7,3] =  Queen.Queen(Color.WHITE)
        self.__positions[7,4] =  King.King(Color.WHITE)
        self.__positions[7,5] =  Bishop.Bishop(Color.WHITE)
        self.__positions[7,6] =  Knight.Knight(Color.WHITE)
        self.__positions[7,7] =  Rook.Rook(Color.WHITE)
        for x in range(8):
            self.__positions[6,x] = Pawn.Pawn(Color.WHITE)

    def isTherePiece(self, row:int, column:int)->Piece:
        row = 7 - row
        column = 7 - column
        return self.__positions[row,column]

    def getPositions(self)-> np:
        return self.__positions