"""Read NHL player data from the statistics API."""

import requests

from player import Player


class PlayerReader:
    """Read player data from the NHL statistics API."""

    def __init__(self, url):
        self.url = url

    def get_players(self):
        """Return the players provided by the configured API endpoint."""
        response = requests.get(self.url, timeout=10).json()
        return [Player(player_dict) for player_dict in response]
