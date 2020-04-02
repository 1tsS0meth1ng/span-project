from unittest import TestCase

from soccerleague.objects.match import Match
from soccerleague.objects.soccerteam import SoccerTeam


class TestMatch(TestCase):

    def test_test_match_init(self):
        # test with valid values
        team_1_name: str = ''
        team_1: SoccerTeam = SoccerTeam(team_1_name)

        team_2_name: str = ''
        team_2: SoccerTeam = SoccerTeam(team_2_name)

        team_1_score: int = 0
        team_2_score: int = 0

        match = Match(team_1, team_1_score, team_2, team_2_score)

        self.assertEqual(match.team_1.team_name, team_1_name)
        self.assertEqual(match.team_2.team_name, team_2_name)
        self.assertEqual(match.team_1_score, team_1_score)
        self.assertEqual(match.team_2_score, team_2_score)
