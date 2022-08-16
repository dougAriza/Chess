import numpy as np
from chess.Color import Color
from chess.Piece import Piece
from chess.pieces import Bishop, King, Knight, Pawn, Queen, Rook

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

    def generateInitialBoard(self)->np:
        self.__positions[0,0] = Rook.Rook(Color.BLACK, [0,0])
        self.__positions[0,1] = Knight.Knight(Color.BLACK, [0,1])
        self.__positions[0,2] = Bishop.Bishop(Color.BLACK, [0,2])
        self.__positions[0,3] = Queen.Queen(Color.BLACK, [0,3])
        self.__positions[0,4] = King.King(Color.BLACK, [0,4])
        self.__positions[0,5] = Bishop.Bishop(Color.BLACK, [0,5])
        self.__positions[0,6] = Knight.Knight(Color.BLACK, [0,6])
        self.__positions[0,7] = Rook.Rook(Color.BLACK, [0,7])
        for x in range(8):
            self.__positions[1,x] = Pawn.Pawn(Color.BLACK, [1,x])

        self.__positions[7,0] = Rook.Rook(Color.WHITE, [7,0])
        self.__positions[7,1] =  Knight.Knight(Color.WHITE, [7,1])
        self.__positions[7,2] =  Bishop.Bishop(Color.WHITE, [7,2])
        self.__positions[7,3] =  Queen.Queen(Color.WHITE, [7,3])
        self.__positions[7,4] =  King.King(Color.WHITE, [7,4])
        self.__positions[7,5] =  Bishop.Bishop(Color.WHITE, [7,5])
        self.__positions[7,6] =  Knight.Knight(Color.WHITE, [7,6])
        self.__positions[7,7] =  Rook.Rook(Color.WHITE, [7,7])
        for x in range(8):
            self.__positions[6,x] = Pawn.Pawn(Color.WHITE, [6,x])

    def isTherePiece(self, position:str)->Piece:
        row = 8 - int(position[1])
        column = (ord(position[0]) - 65)
        return self.__positions[row,column]

    def getPositions(self)-> np:
        return self.__positions