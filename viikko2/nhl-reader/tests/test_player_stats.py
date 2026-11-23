"""Unit tests for PlayerStats using a local reader stub."""

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    """Provide players without making an API request."""

    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def make_player(name, nationality, team, goals, assists):
    """Create a Player with the fields expected from the API."""
    return Player({
        "name": name,
        "nationality": nationality,
        "team": team,
        "goals": goals,
        "assists": assists,
        "games": 10,
        "id": name,
    })


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            make_player("A", "FIN", "AAA", 10, 20),
            make_player("B", "USA", "BBB", 25, 5),
            make_player("C", "FIN", "BBB", 15, 20),
            make_player("D", "CAN", "AAA", 31, 0),
        ]
        self.stats = PlayerStats(PlayerReaderStub(self.players))

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(["C", "A"], [player.name for player in result])

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(["D", "A"], [player.name for player in result])

    def test_top_goal_scorers_sorts_by_goals_and_limits_results(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual(["D", "B"], [player.name for player in result])

    def test_top_goal_scorers_returns_empty_list_for_zero_limit(self):
        self.assertEqual([], self.stats.top_goal_scorers(0))

    def test_filters_return_empty_list_when_there_are_no_matches(self):
        self.assertEqual([], self.stats.top_scorers_by_team("ZZZ"))
        self.assertEqual([], self.stats.top_scorers_by_nationality("ZZZ"))


if __name__ == "__main__":
    unittest.main()
