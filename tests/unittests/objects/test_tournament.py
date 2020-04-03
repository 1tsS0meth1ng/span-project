from unittest import TestCase

from soccerleague.objects.soccermatch import Match
from soccerleague.objects.soccerteam import SoccerTeam

from importlib.resources import open_text
from random import randint, choices

from soccerleague.objects.tournament import Tournament


class TestTournament(TestCase):

    def setUp(self):
        self.teams = []

        with open_text('resources', 'teams.txt') as team_reader:
            for team_text in team_reader.readlines():
                self.teams.append(SoccerTeam(team_text.replace('\n', '')))

        self.matches = set()
        self.leader_board = {}

        self.match_draw = Match(self.teams[0], 0, self.teams[1], 0)
        self.match_team_2_win_team_3 = Match(self.teams[1], 1, self.teams[2], 0)
        self.match_team_1_win_team_2 = Match(self.teams[2], 3, self.teams[1], 2)

        for counter in range(len(self.teams) * 10):
            team_1, team_2 = choices(self.teams, k=2)
            score_1 = randint(0, 10)
            score_2 = randint(0, 10)

            match = Match(team_1, score_1, team_2, score_2)
            self.matches.add(match)
            winner = match.get_winner()
            loser = match.get_loser()
            if winner is not None:
                if self.leader_board.get(winner) is None:
                    self.leader_board[winner] = 3
                else:
                    self.leader_board[winner] += 3

                if self.leader_board.get(loser) is None:
                    self.leader_board[loser] = 0
            else:

                if self.leader_board.get(match.team_1) is None:
                    self.leader_board[match.team_1] = 1
                else:
                    self.leader_board[match.team_1] += 1

                if self.leader_board.get(match.team_2) is None:
                    self.leader_board[match.team_2] = 1
                else:
                    self.leader_board[match.team_2] += 1

    def test_init(self):
        league_name = 'Test League'
        league = Tournament(league_name)
        self.assertEqual(league.league_name, league_name)

        # test empty league name
        empty_league_name = ''
        with self.assertRaises(ValueError):
            league = Tournament(empty_league_name)

        # test incorrect league name type
        incorrect_league_name_type = None
        with self.assertRaises(TypeError):
            league = Tournament(incorrect_league_name_type)

    def test_matches(self):
        # test no matches added
        league_name = 'Test League'
        league = Tournament(league_name)
        self.assertSetEqual(league.matches, set())

        # test matches setter should not be settable
        with self.assertRaises(AttributeError):
            league.matches = {1, 2, 3}

        # test add multiple matches
        league_name_2 = 'Test League'
        league_2 = Tournament(league_name_2)
        self.assertSetEqual(league_2.matches, set())

        for i in self.matches:
            league_2.add_match(i)
        self.assertSetEqual(league_2.matches, self.matches)

    def test_leader_board(self):
        league_name = 'Test League'
        league = Tournament(league_name)
        self.assertEqual(league.leader_board, [])

        for match in self.matches:
            league.add_match(match)

        self.assertListEqual(league.leader_board, self.leader_board)
