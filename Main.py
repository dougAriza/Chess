from numpy import isin
from entities.Match import Match
from entities.Piece import Piece
from entities.pieces.Rook import Rook
from ui.ChessBoard import ChessBoard

# chessBoard = ChessBoard()

match = Match()
boardPos = match.getBoard().getPositions()

for i in range(8):
    s=""
    for j in range(8):
        s += boardPos[i,j].__str__() + " "
    print(s)


