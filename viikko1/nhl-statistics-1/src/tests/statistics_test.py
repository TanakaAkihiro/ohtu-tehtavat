import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    def test_search_by_name_successfully(self):
        self.assertAlmostEqual(str(self.statistics.search("Semenko")), "Semenko EDM 4 + 12 = 16")
    
    def test_search_by_unknown_name(self):
        self.assertIsNone(self.statistics.search("Selänne"))

    def test_search_by_team_name(self):
        self.assertAlmostEqual(str(self.statistics.team("DET")[0]), "Yzerman DET 42 + 56 = 98")

    def test_search_the_best_scorer(self):
        self.assertAlmostEqual(str(self.statistics.top_scorers(1)[0]), "Gretzky EDM 35 + 89 = 124")