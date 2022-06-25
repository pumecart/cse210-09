from game.casting.actor import Actor
from game.casting.score import Score
from game.shared.point import Point


class Score2(Score):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by beating the other player.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)
        self._position = Point(825, 0)