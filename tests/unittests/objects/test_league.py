from unittest import TestCase

from soccerleague.objects.league import League


class TestLeague(TestCase):

    def test_init(self):
        league_name = 'Test League'
        league = League(league_name)
        self.assertEqual(league.league_name, league_name)

        # test empty league name
        empty_league_name = ''
        with self.assertRaises(ValueError):
            league = League(empty_league_name)

        # test empty league name
        incorrect_league_name_type = None
        with self.assertRaises(TypeError):
            league = League(incorrect_league_name_type)
