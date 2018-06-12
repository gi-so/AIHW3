import time
import random

ids = ["935885178", "203609177"]


class PacmanController:
    """This class is a controller for a pacman agent."""

    def __init__(self, state, steps):
        """Initialize controller for given the initial setting.
        This method MUST terminate within the specified timeout."""
        # print('COMPLETE init ')

    def choose_next_action(self, state, accumulated_reward):
        """Choose next action for pacman controller given the current state.
        Action should be returned in the format described previous parts of the project.
        This method MUST terminate within the specified timeout.
        """

        "random walk agent"
        alive = False
        for row in state:
            for cell in row:
                if cell == 66:
                    alive = True
                    break
            if alive:
                break
        if not alive:
            return "reset"
        return random.choice(["U", "D", "L", "R"])
        # print('COMPLETE choose_next_action')
