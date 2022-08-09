from numpy import isin
from entities.Match import Match
from entities.Piece import Piece
from entities.pieces.Rook import Rook
from ui.ChessBoard import ChessBoard

# chessBoard = ChessBoard()

match = Match()
# print(match.getBoard())

piece = match.getBoard().isTherePiece("E1")

print(match.getBoard())
print(piece)
# print(piece.getColor())