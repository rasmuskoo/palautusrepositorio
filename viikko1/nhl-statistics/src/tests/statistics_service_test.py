import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_olemassa_olevan_pelaajan(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.points, 90)

    def test_search_palauttaa_none_jos_pelaajaa_ei_ole(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team_palauttaa_joukkueen_pelaajat(self):
        names = [player.name for player in self.stats.team("EDM")]

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_palauttaa_tyhjan_listan_tuntemattomalle_joukkueelle(self):
        self.assertEqual(self.stats.team("WPG"), [])

    def test_top_palauttaa_pelaajat_pistejarjestyksessa(self):
        top = self.stats.top(3)

        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_pisteiden_perusteella(self):
        top = self.stats.top(3, SortBy.POINTS)

        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_maalien_perusteella(self):
        top = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(top[0].name, "Lemieux")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Kurri")

    def test_top_syottojen_perusteella(self):
        top = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Lemieux")
