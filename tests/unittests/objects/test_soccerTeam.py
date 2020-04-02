from unittest import TestCase

from soccerleague.objects.soccerteam import SoccerTeam


class TestSoccerTeam(TestCase):

    def test_init(self):
        team_name: str = 'Some Team Name'
        soccer_team = SoccerTeam(team_name)
        self.assertEqual(soccer_team.team_name, team_name)

        with self.assertRaises(TypeError):
            value: int = 12345
            soccer_team = SoccerTeam(value)

    def test_team_name_property(self):
        team_name: str = 'Some Team Name'
        soccer_team: SoccerTeam = SoccerTeam(team_name)
        # test getter
        self.assertEqual(soccer_team.team_name, team_name)

        # test setter when correct type (str)
        new_team_name: str = 'A New Team Name'
        soccer_team.team_name = new_team_name
        self.assertEqual(soccer_team.team_name, new_team_name)

        # test setter when incorrect input (incorrect type)
        new_incorrect_team_name: int = 1234565

        with self.assertRaises(TypeError):
            soccer_team.team_name = new_incorrect_team_name
