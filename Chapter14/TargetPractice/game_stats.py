class GameStats:
    """Track statistics for Target Practice"""

    def __init__(self, tp_game):
        """Initialize the statistics"""
        self.settings = tp_game.settings
        self.reset_stats()

        #Start Target Practice in an active state
        self.game_active = False
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.orbs_left = self.settings.orbs_limit