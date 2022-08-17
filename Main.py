
from board.Board import Board
from board.Position import Position
from chess.Color import Color
from chess.Match import Match
from chess.MatchException import MatchException
from chess.pieces.King import King

match = Match(Board())
print(match.getBoard())

# king = King(Color.WHITE,Position(0,4))
# print(king.possibleMoves())