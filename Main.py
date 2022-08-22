
from board.Board import Board
from board.Position import Position
from chess.Color import Color
from chess.Match import Match
from chess.pieces.King import King

# match = Match(Board())
# print(match.getBoard())

board = Board()
king = King(Color.WHITE,Position(0,4), board)
print(king.possibleMoves())