import py
import constants
from game.scripting.control_actor1_action import ControlActor1Action
from game.shared.point import Point


class ControlActor2Action(ControlActor1Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        super().__init__()
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        snake1 = cast.get_first_actor("snakes1")
        snake2 = cast.get_first_actor("snakes2")
        snake1.turn_head(self._direction)
        snake2.turn_head(self._direction)