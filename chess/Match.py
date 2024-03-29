from board.Board import Board
from board.Position import Position
from chess.MatchException import MatchException
from chess.Color import Color
from chess.pieces import Bishop, King, Knight, Pawn, Queen, Rook

class Match:
    def __init__(self,board:Board) -> None:
        self.__turn:int = 1
        self.__board = board
        self.generateInitialBoard()
   
    def __incremmentTurn(self):
        self.__turn += 1

    def getTurn(self)->int:
        return self.__turn
             
    def getBoard(self)->Board:
        return self.__board

    def generateInitialBoard(self):
        self.__board.putPiece(Rook.Rook(Color.BLACK, Position(0,0),self.__board), Position(0,0))
        self.__board.putPiece(Knight.Knight(Color.BLACK, Position(0,1), self.__board), Position(0,1))
        self.__board.putPiece(Bishop.Bishop(Color.BLACK, Position(0,2), self.__board), Position(0,2))
        self.__board.putPiece(Queen.Queen(Color.BLACK, Position(0,3), self.__board), Position(0,3))
        self.__board.putPiece(King.King(Color.BLACK, Position(0,4), self.__board), Position(0,4))
        self.__board.putPiece(Bishop.Bishop(Color.BLACK, Position(0,5), self.__board), Position(0,5))
        self.__board.putPiece(Knight.Knight(Color.BLACK, Position(0,6), self.__board), Position(0,6))
        self.__board.putPiece(Rook.Rook(Color.BLACK, Position(0,7), self.__board), Position(0,7))
        for x in range(8):
            self.__board.putPiece(Pawn.Pawn(Color.BLACK, Position(1,x), self.__board),Position(1,x))

        self.__board.putPiece(Rook.Rook(Color.WHITE, Position(7,0), self.__board), Position(7,0))
        self.__board.putPiece(Knight.Knight(Color.WHITE, Position(7,1), self.__board), Position(7,1))
        self.__board.putPiece(Bishop.Bishop(Color.WHITE, Position(7,2), self.__board), Position(7,2))
        self.__board.putPiece(Queen.Queen(Color.WHITE, Position(7,3), self.__board), Position(7,3))
        self.__board.putPiece(King.King(Color.WHITE, Position(7,4), self.__board), Position(7,4))
        self.__board.putPiece(Bishop.Bishop(Color.WHITE, Position(7,5), self.__board), Position(7,5))
        self.__board.putPiece(Knight.Knight(Color.WHITE, Position(7,6), self.__board), Position(7,6))
        self.__board.putPiece(Rook.Rook(Color.WHITE, Position(7,7), self.__board), Position(7,7))
        for x in range(8):
            self.__board.putPiece(Pawn.Pawn(Color.WHITE, Position(6,x), self.__board),Position(6,x))

    def selectPosition(self, position:str):
        piece = self.__board.isTherePiece(position)
        if (piece == None):
            raise MatchException("There isn't a piece in this position!")
        elif ((piece.getColor() == Color.BLACK) and (self.__turn % 2 != 0)):
            raise MatchException("It is a white piece!")
        elif ((piece.getColor() == Color.WHITE) and (self.__turn % 2 == 0)):
            raise MatchException("It is a black piece!")