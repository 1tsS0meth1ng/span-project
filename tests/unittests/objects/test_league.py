from unittest import TestCase

from soccerleague.objects import Match
from soccerleague.objects.league import League
from soccerleague.objects.soccerteam import SoccerTeam


class TestLeague(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.team_1 = SoccerTeam('team 1')
        self.team_2 = SoccerTeam('team 2')
        self.team_3 = SoccerTeam('team 3')
        self.team_4 = SoccerTeam('team 4')
        self.team_5 = SoccerTeam('team 5')
        self.team_6 = SoccerTeam('team 6')
        self.team_7 = SoccerTeam('team 7')

        self.matches = []

        self.match_draw = Match(self.team_1, 0, self.team_2, 0)
        self.match_team_2_win_team_3 = Match(self.team_2, 1, self.team_3, 0)
        self.match_team_1_win_team_2 = Match(self.team_1, 3, self.team_2, 2)

        self.matches.append(self.match_draw)
        self.matches.append(self.match_team_2_win_team_3)
        self.matches.append(self.match_team_1_win_team_2)

    def test_init(self):
        league_name = 'Test League'
        league = League(league_name)
        self.assertEqual(league.league_name, league_name)

        # test empty league name
        empty_league_name = ''
        with self.assertRaises(ValueError):
            league = League(empty_league_name)

        # test incorrect league name type
        incorrect_league_name_type = None
        with self.assertRaises(TypeError):
            league = League(incorrect_league_name_type)

    def test_matches(self):
        # test no matches added
        league_name = 'Test League'
        league = League(league_name)
        self.assertEqual(league.matches, [])

        # test matches setter should not be settable
        with self.assertRaises(AttributeError):
            league.matches = []

        # test match add
        league.add_match(self.match_draw)
        match_list_1 = [self.match_draw]
        self.assertEqual(league.matches, match_list_1)

        # test add multiple
        league_name_2 = 'Test League'
        league_2 = League(league_name_2)

        for i in self.matches:
            league_2.add_match(i)

        self.assertEqual(league_2.matches, self.matches)
