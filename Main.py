
from board.Board import Board
from board.Position import Position
from chess.Color import Color
from chess.Match import Match
from chess.pieces.King import King

board = Board()
match = Match(board)
print(match.getBoard())

# king = King(Color.WHITE,Position(0,4), board)
# print(king.possibleMoves())