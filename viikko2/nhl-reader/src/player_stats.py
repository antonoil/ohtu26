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
