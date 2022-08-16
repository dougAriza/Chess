from board.Board import Board
from chess.MatchException import MatchException
from chess.Color import Color

class Match:
    def __init__(self,board:Board) -> None:
        self.__turn:int = 1
        self.__board = board
        board.generateInitialBoard()
   
    def __incremmentTurn(self):
        self.__turn += 1

    def getTurn(self)->int:
        return self.__turn
             
    def getBoard(self)->Board:
        return self.__board

    def selectPosition(self, position:str):
        piece = self.__board.isTherePiece(position)
        if (piece == None):
            raise MatchException("There isn't a piece in this position!")
        elif ((piece.getColor() == Color.BLACK) and (self.__turn % 2 != 0)):
            raise MatchException("It is a white piece!")
        elif ((piece.getColor() == Color.WHITE) and (self.__turn % 2 == 0)):
            raise MatchException("It is a black piece!")