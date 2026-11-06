from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

SEASONS = [f"{year}-{(year + 1) % 100:02}" for year in range(2018, 2027)]

def players_table(players, season, nationality):
    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("name", style="cyan")
    table.add_column("teams", style="magenta")
    table.add_column("goals", style="green", justify="right")
    table.add_column("assists", style="green", justify="right")
    table.add_column("points", style="green", justify="right")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    return table

def main():
    console = Console()

    season = Prompt.ask("Season", choices=SEASONS, default="2024-25")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = stats.nationalities()

    while True:
        nationality = Prompt.ask("Nationality", choices=nationalities, default="", case_sensitive=False)

        if not nationality:
            break

        players = stats.top_scorers_by_nationality(nationality)
        console.print(players_table(players, season, nationality))

if __name__ == "__main__":
    main()
