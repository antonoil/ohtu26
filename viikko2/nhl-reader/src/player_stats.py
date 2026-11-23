"""Calculate scoring statistics for NHL players."""

from player_reader import PlayerReader


class PlayerStats:
    """Calculate statistics for players returned by a reader."""

    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        """Return players of a nationality ordered by points, descending."""
        players = [
            player for player in self.reader.get_players()
            if player.nationality == nationality
        ]
        return sorted(players, key=lambda player: player.goals + player.assists, reverse=True)

    def top_scorers_by_team(self, team):
        """Return players from a team ordered by points, descending."""
        players = [
            player for player in self.reader.get_players()
            if player.team == team
        ]
        return sorted(players, key=lambda player: player.goals + player.assists, reverse=True)

    def top_goal_scorers(self, how_many):
        """Return up to how_many players ordered by goals, descending."""
        players = sorted(
            self.reader.get_players(),
            key=lambda player: player.goals,
            reverse=True,
        )
        return players[:how_many]
