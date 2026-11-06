class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def nationalities(self):
        return list(dict.fromkeys(player.nationality for player in self.players))

    def top_scorers_by_nationality(self, nationality):
        filtered = [player for player in self.players if player.nationality == nationality]

        return sorted(filtered, key=lambda player: player.points, reverse=True)
