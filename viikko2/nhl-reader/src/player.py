"""Represent NHL players and their season statistics."""


class Player:
    """Represent an NHL player and their season statistics."""

    def __init__(self, player_data):
        """Initialize a player from one API response object."""
        self.name = player_data['name']
        self.nationality = player_data['nationality']
        self.assists = player_data['assists']
        self.goals = player_data['goals']
        self.team = player_data['team']
        self.games = player_data['games']
        self.id = player_data['id']

    def __str__(self):
        """Return a readable summary of the player and their points."""
        return f"{self.name}, {self.nationality}, {self.goals} + {self.assists}, {self.goals + self.assists}"
