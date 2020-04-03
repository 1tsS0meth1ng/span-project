from unittest import TestCase

from soccerleague import SoccerMatch
from soccerleague import SoccerTeam


class TestMatch(TestCase):

    def test_test_match_init(self):
        # test with valid values
        team_1_name: str = ''
        team_1: SoccerTeam = SoccerTeam(team_1_name)

        team_2_name: str = ''
        team_2: SoccerTeam = SoccerTeam(team_2_name)

        team_1_score: int = 0
        team_2_score: int = 0

        match = SoccerMatch(team_1, team_1_score, team_2, team_2_score)

        self.assertEqual(match.team_1.competitor_name, team_1_name)
        self.assertEqual(match.team_2.competitor_name, team_2_name)
        self.assertEqual(match.team_1_score, team_1_score)
        self.assertEqual(match.team_2_score, team_2_score)

        # test with invalid values

        with self.assertRaises(TypeError):
            match = SoccerMatch(0, '1', 0, '')

        # test with negative score 1
        score_value = -1
        with self.assertRaises(TypeError):
            match = SoccerMatch(team_1, score_value, team_2, team_2_score)

        # test with negative score 1
        with self.assertRaises(TypeError):
            match = SoccerMatch(team_1, team_1_score, team_2, score_value)

    def test_winner_loser_function(self):
        # test with valid values
        team_1_name: str = ''
        team_1: SoccerTeam = SoccerTeam(team_1_name)

        team_2_name: str = ''
        team_2: SoccerTeam = SoccerTeam(team_2_name)

        win_score: int = 6
        lose_score: int = 0
        draw_score: int = 2

        # test win on team 1

        match_1 = SoccerMatch(team_1, win_score, team_2, lose_score)
        winner_1 = match_1.get_winner()
        loser_1 = match_1.get_loser()

        self.assertEqual(winner_1, team_1)
        self.assertEqual(loser_1, team_2)

        # test win on team 2
        match_2 = SoccerMatch(team_1, lose_score, team_2, win_score)
        winner_2 = match_2.get_winner()
        loser_2 = match_2.get_loser()

        self.assertEqual(winner_2, team_2)
        self.assertEqual(loser_2, team_1)

        # test draw
        match_3 = SoccerMatch(team_1, draw_score, team_2, draw_score)
        winner_3 = match_3.get_winner()
        loser_3 = match_3.get_loser()

        self.assertEqual(winner_3, None)
        self.assertEqual(loser_3, None)
