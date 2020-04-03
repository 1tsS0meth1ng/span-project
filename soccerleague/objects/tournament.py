from abc import ABC, abstractmethod

from soccerleague.objects.soccermatch import Match


class Tournament(ABC):
    __league_name: str = None
    __leader_board: dict = {}
    __matches: set = set()

    def __init__(self, name):
        self.league_name = name

    @property
    def league_name(self):
        return self.__league_name

    @league_name.setter
    def league_name(self, value: str):
        if type(value) is str:
            if value != '':
                self.__league_name = value
            else:
                raise ValueError('League name cannot be an empty string')
        else:
            raise TypeError('League name needs to be of type str')

    @property
    def matches(self) -> set:
        return self.__matches

    def add_match(self, match: Match):
        winner = match.get_winner()
        loser = match.get_loser()
        if winner is not None:
            if self.__leader_board.get(winner) is None:
                self.__leader_board[winner] = 3
            else:
                self.__leader_board[winner] += 3

            if self.__leader_board.get(loser) is None:
                self.__leader_board[loser] = 0
        else:

            if self.__leader_board.get(match.team_1) is None:
                self.__leader_board[match.team_1] = 1
            else:
                self.__leader_board[match.team_1] += 1

            if self.__leader_board.get(match.team_2) is None:
                self.__leader_board[match.team_2] = 1
            else:
                self.__leader_board[match.team_2] += 1
        self.__matches.add(match)

    @property
    def leader_board(self) -> list:
        return self.leader_board_output(self.__leader_board)

    @abstractmethod
    def leader_board_output(self, leader_board):
        pass
