class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, sr_game):
        """Initialize the statistics"""
        self.settings = sr_game.settings
        self.reset_stats()

        #start the sideways rocket game in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize stastistics that can change during the game."""
        self.rockets_left = self.settings.rocket_limit
