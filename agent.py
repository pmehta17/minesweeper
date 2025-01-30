
from utils import Action, ActionType, Cell, Condition
import random

class Agent:
    def __init__(self, game):
        """
        Initializes the agent with the given game instance.

        Args:
            game: An instance of the game that the agent will interact with.
        """
        self.game = game

    def get_next_action(self, obs):
        """
        Determines the next action to take based on the given observation.

        Args:
            obs: The current observation from the environment.

        Returns:
            The next action to take.

        Raises:
            NotImplementedError: This method should be overridden by subclasses.
        """
        raise NotImplementedError()

    def play(self):
        """
        Executes the game loop for the agent.

        The agent continuously observes the game state, determines the next action,
        and performs the action until the game reaches a terminal condition.

        Returns:
            goal_test (Condition): The final state of the game, indicating whether
                                   the game is still in progress, won, or reveal a bomb.
        """
        obs = self.game.obs()
        while True:
            action = self.get_next_action(obs)
            obs, goal_test = self.game.step(action)
            if goal_test != Condition.IN_PROGRESS:
                break
        return goal_test

    def get_neighbors(self, x, y):
        """
        Get the neighboring coordinates of a given cell in a board.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            list of tuple: A list of tuples representing the coordinates of the neighboring cells.
                           Only includes neighbors that are within the bounds of the board.
        """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < self.size and 0 <= y + dy < self.size]


class ManualGuiAgent(Agent):
    def __init__(self, game):
        super().__init__(game)

    def play(self):
        pass


class RuleBasedAgent(Agent):
    def __init__(self, game):
        super().__init__(game)
        self.size = game.size

    def get_next_action(self, obs):
        ### IMPLEMENT THIS ###
        # 1. Look for certain patterns in revealed integer cells
        """
        A minimal approach:
        1) Scan from top-left to bottom-right.
        2) Reveal the first cell that is still unrevealed.
        3) If everything is revealed, return a fallback action.
        """
        for x in range(self.size):
            for y in range(self.size):
                if obs[x][y] == Cell.UNREVEALED:
                    # Reveal the first unrevealed cell we find
                    return Action(ActionType.REVEAL, x, y)

        # Fallback if no unrevealed cells remain
        return Action(ActionType.REVEAL, 0, 0)
