from abc import ABC, abstractmethod

from soccerleague.businessobjects.matches.match import Match
from soccerleague.businessobjects.competitors.competitor import Competitor


class Tournament(ABC):
    """ A class to represent a tournament
    Attributes
    ----------
    __tournament_name : str
        The name of the tournament
    _leader_board : dict
        The unordered leader board of the tournament
    __matches : set
        The set of matches that has been played in the tournament
    """

    def __init__(self, name):
        """ Initializer for the Tournament class

        Parameters
        ----------
        name
            The name of the tournament
        """
        self.__tournament_name: str = None
        self._leader_board: dict = {}
        self.__matches: set = set()
        self.tournament_name = name

    @property
    def tournament_name(self):
        """league_name: str object which represents the tournament's name

        The setter checks if the correct type str is being set else it raises a TypeError
        """
        return self.__tournament_name

    @tournament_name.setter
    def tournament_name(self, value: str):
        print('setting name: '+value)
        if type(value) is str:
            self.__tournament_name = value
        else:
            raise TypeError('League name needs to be of type str')

    @property
    def matches(self) -> set:
        """ A property that returns the set of matches that have been played

        Returns
        -------
        set
            The set of matches played
        """
        return self.__matches

    def add_match(self, match: Match):
        """ A method which adds matches to the match set while modifying the competitors scores

        Parameters
        ----------
        match
            The match to be added
        """
        winner = match.get_winner()
        loser = match.get_loser()
        self.increment_score(winner, loser, match)
        self.__matches.add(match)

    @abstractmethod
    def increment_score(self, winner: Competitor, loser: Competitor, match: Match):
        """ An abstract method which is injected into add_match to increment the scores of a competitor

        Parameters
        ----------
        winner : Competitor
            The winner of the competition. Can be None
        loser : Competitor
            The loser of the competition. Can be None
        match : Match
            The original match object
        """
        pass

    @property
    def leader_board(self) -> list:
        """leader_board: list object which represents the formatted leader board

        """
        return self.leader_board_output(self._leader_board)

    @abstractmethod
    def leader_board_output(self, leader_board: dict) -> list:
        """ An abstract method when implemented should return the leader board with a specified format

        Parameters
        ----------
        leader_board : dict
            the input leader board which will be used to create the formatted list
        Returns
        -------
        list
            The formatted list which is returned
        """
        pass
