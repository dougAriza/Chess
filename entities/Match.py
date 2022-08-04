from entities.Board import Board

class Match:
    def __init__(self, board:Board) -> None:
        self.__turn:int
        self.__board = board
   
    def incremmentTurn(self):
        self.__turn += 1

    def getTurn(self)->int:
        return self.__turn
             
    def getBoard(self)->Board:
        return self.__board