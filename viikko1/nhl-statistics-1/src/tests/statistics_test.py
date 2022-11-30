import unittest
from statistics import Statistics
from stub_player_reader import StubPlayerReader
from player import Player


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(
            reader = StubPlayerReader()
        )
        self.player = self.stats.search("Tomas Tatar")


    def test_absent_player_is_searched_but_not_found(self):
        self.assertEqual(self.stats.search("Ilari Haho"), None)

    def test_team_list_is_returned_on_search(self):
        players_of_team = self.stats.team("PHI")
        self.assertEqual(len(players_of_team), 36)

    def test_top_method_returns_correct_list(self):
        top_2_players = self.stats.top(2)
        player1 = self.stats.search("Johnny Gaudreau")
        player2 = self.stats.search("Jonathan Huberdeau")
        player3 = self.stats.search("Connor McDavid")
        list = []
        list.append(player1)
        list.append(player2)
        list.append(player3)
        self.assertCountEqual(top_2_players, list)

    

    

