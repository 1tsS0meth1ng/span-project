from typing import Optional
from unittest import TestCase

from soccerleague import Match
from soccerleague import SoccerTeam

from importlib.resources import open_text
from random import randint, choices

from soccerleague import Tournament
from soccerleague.businessobjects.competitors import Competitor


class TestMatch(Match):

    def get_loser(self) -> Optional[Competitor]:
        pass

    def get_winner(self) -> Optional[Competitor]:
        pass


class TestTournamentClass(Tournament):

    def increment_score(self, winner, loser, match):
        pass

    def leader_board_output(self, leader_board):
        pass


class TestTournament(TestCase):

    def setUp(self):
        self.teams = []

        with open_text('resources', 'teams.txt') as team_reader:
            for team_text in team_reader.readlines():
                self.teams.append(SoccerTeam(team_text.replace('\n', '')))

        self.matches = set()
        self.leader_board = {}

        self.match_draw = TestMatch(self.teams[0], 0, self.teams[1], 0)
        self.match_team_2_win_team_3 = TestMatch(self.teams[1], 1, self.teams[2], 0)
        self.match_team_1_win_team_2 = TestMatch(self.teams[2], 3, self.teams[1], 2)

        for counter in range(len(self.teams) * 10):
            team_1, team_2 = choices(self.teams, k=2)
            score_1 = randint(0, 10)
            score_2 = randint(0, 10)

            match = TestMatch(team_1, score_1, team_2, score_2)
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
        league = TestTournamentClass(league_name)
        self.assertEqual(league.league_name, league_name)

    def test_matches(self):
        # test no matches added
        league_name = 'Test League'
        league = TestTournamentClass(league_name)
        self.assertSetEqual(league.matches, set())

        # test matches setter should not be settable
        with self.assertRaises(AttributeError):
            league.matches = {1, 2, 3}

        # test add multiple matches
        league_name_2 = 'Test League'
        league_2 = TestTournamentClass(league_name_2)
        self.assertSetEqual(league_2.matches, set())

        for i in self.matches:
            league_2.add_match(i)
        self.assertSetEqual(league_2.matches, self.matches)

