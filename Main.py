
from chess.Color import Color
from chess.Match import Match
from chess.MatchException import MatchException
from chess.pieces.King import King

# match = Match()

king = King(Color.WHITE,[0,4])
print(king.possibleMoves())