"""Display NHL scoring leaders for a selected nationality."""

from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    """Fetch and display top scorers by nationality or team."""
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    selection = input("List by nationality (1) or team (2)? ")
    if selection == "2":
        value = input("Team abbreviation: ")
        players = stats.top_scorers_by_team(value)
        title = f"Top NHL Scorers from {value}"
    else:
        value = input("Nationality [USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]: ")
        players = stats.top_scorers_by_nationality(value)
        title = f"Top NHL Scorers from {value}"

    table = Table(title=title)
    table.add_column("Name", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists),
        )

    Console().print(table)
