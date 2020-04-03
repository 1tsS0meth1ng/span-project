import uuid
from abc import ABC, abstractmethod
from typing import Optional

from soccerleague.businessobjects.competitors.competitor import Competitor


class Match(ABC):
    """ A match with both teams and both teams scores
        Attributes
        ----------
        __team_1 : Competitor
            A private variable holding the first competitor in the match
        __team_2 : Competitor
            A private variable holding the second competitor in the match
        __team_1_score : int
            A private variable holding the first competitor's score in the match
        __team_2_score : int
            A private variable holding the second competitor's score in the match
    """

    def __init__(self, team_1: Competitor, team_1_score: int, team_2: Competitor, team_2_score: int):
        """

        Parameters
        ----------
        team_1 : Competitor
            The first competitor in the match
        team_1_score : int
            The first teams score
        team_2 : Competitor
            The second competitor in the match
        team_2_score : int
            The second teams score

        Raises
        ------
        TypeException
            Incorrect Parameter Types
        """
        self.__team_1: Competitor = None
        self.__team_2: Competitor = None
        self.__team_1_score: int = None
        self.__team_2_score: int = None
        self.__match_id: uuid = uuid.uuid4()

        self.team_1 = team_1
        self.team_1_score = team_1_score
        self.team_2 = team_2
        self.team_2_score = team_2_score

    @property
    def team_1(self) -> Competitor:
        """team_1: Soccer Team object for the first soccer team

        The setter checks if the correct type (SoccerTeam) is being set else it raises a TypeError
        """

        return self.__team_1

    @team_1.setter
    def team_1(self, team: Competitor):
        if isinstance(team, Competitor):
            self.__team_1 = team
        else:
            raise TypeError('Team 1 needs to be of type Team')

    @property
    def team_2(self) -> Competitor:
        """team_2: Soccer Team object for the second soccer team

        The setter checks if the correct type (SoccerTeam) is being set else it raises a TypeError
        """
        return self.__team_2

    @team_2.setter
    def team_2(self, team: Competitor):
        if isinstance(team, Competitor):
            self.__team_2 = team
        else:
            raise TypeError('Team 2 needs to be of type Team')

    @property
    def team_1_score(self) -> int:
        """team_1_score: Int object which represents team 1's score

        The setter checks if the correct type (int) is being set and the value is non-negative
        else it raises a TypeError
        """
        return self.__team_1_score

    @team_1_score.setter
    def team_1_score(self, value: int):
        if type(value) is int:
            if value >= 0:
                self.__team_1_score = value
            else:
                raise TypeError('Score 1 cannot be negative')
        else:
            raise TypeError('Score 1 needs to be of type int')

    @property
    def team_2_score(self) -> int:
        """team_2_score: Int object which represents team 2's score

        The setter checks if the correct type (int) is being set and the value is non-negative
        else it raises a TypeError
        """
        return self.__team_2_score

    @team_2_score.setter
    def team_2_score(self, value: int):
        if type(value) is int:
            if value >= 0:
                self.__team_2_score = value
            else:
                raise TypeError('Score 2 cannot be negative')
        else:
            raise TypeError('Score 2 needs to be of type int')

    @property
    def match_id(self):
        """ match_id: uuid object which represents the matches id
        """
        return self.__match_id

    @abstractmethod
    def get_winner(self) -> Optional[Competitor]:
        """ A function which determines which competitor has won using their scores

        Returns
        -------
        Optional[Competitor]
            Returns the winning soccer team else if it is a draw. returns None
        """
        pass

    @abstractmethod
    def get_loser(self) -> Optional[Competitor]:
        """ A function which determines which competitor has lost using their scores

        Returns
        -------
        Optional[Competitor]
            Returns the losing competitor else if it is a draw. returns None
        """
        pass

    def __eq__(self, other):
        if other.id == self.id and other.team_1 == self.team_1 and other.team_2 == self.team_2 and \
                other.team_1_score == self.team_1_score and other.team_2_score == self.team_2_score:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__repr__())
