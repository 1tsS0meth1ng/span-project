from typing import Optional

from soccerleague.objects.soccerteam import SoccerTeam


class Match:
    """ A match with both teams and both teams scores

    """
    __team_1: SoccerTeam = None
    __team_2: SoccerTeam = None
    __team_1_score: int = None
    __team_2_score: int = None

    def __init__(self, team_1: SoccerTeam, team_1_score: int, team_2: SoccerTeam, team_2_score: int):
        """

        Parameters
        ----------
        team_1 : SoccerTeam
            The first team in the match
        team_1_score : int
            The first teams score
        team_2 : SoccerTeam
            The second team in the match
        team_2_score : int
            The second teams score

        Raises
        ------
        TypeException
            Incorrect Parameter Types
        """
        self.team_1 = team_1
        self.team_1_score = team_1_score
        self.team_2 = team_2
        self.team_2_score = team_2_score

    @property
    def team_1(self) -> SoccerTeam:
        """team_1: Soccer Team object for the first soccer team

        The setter checks if the correct type (SoccerTeam) is being set else it raises a TypeError
        """

        return self.__team_1

    @team_1.setter
    def team_1(self, team: SoccerTeam):
        if type(team) is SoccerTeam:
            self.__team_1 = team
        else:
            raise TypeError('Team 1 needs to be of type Team')

    @property
    def team_2(self) -> SoccerTeam:
        """team_2: Soccer Team object for the second soccer team

        The setter checks if the correct type (SoccerTeam) is being set else it raises a TypeError
        """
        return self.__team_2

    @team_2.setter
    def team_2(self, team: SoccerTeam):
        if type(team) is SoccerTeam:
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

    def get_winner(self) -> Optional[SoccerTeam]:
        """ A function which determines which Soccer Team has won using their scores

        The function compares the team 1's score and team 2's score by subtracting the values.
        It then compares the values to 0(ie >, <).
        if > then team 1 won
        if < then team 2 won
        else then a draw and nobody won

        Returns
        -------
        Optional[SoccerTeam]
            Returns the winning soccer team else if it is a draw. returns None
        """
        difference = self.__team_1_score - self.__team_2_score

        if difference > 0:
            return self.__team_1
        elif difference < 0:
            return self.__team_2
        else:
            return None

    def get_loser(self) -> Optional[SoccerTeam]:
        """ A function which determines which Soccer Team has lost using their scores

        The function compares the team 1's score and team 2's score by subtracting the values.
        It then compares the values to 0(ie >, <).
        if > then team 1 lost
        if < then team 2 lost
        else then a draw and nobody lost

        Returns
        -------
        Optional[SoccerTeam]
            Returns the losing soccer team else if it is a draw. returns None
        """
        difference = self.__team_1_score - self.__team_2_score

        if difference > 0:
            return self.__team_2
        elif difference < 0:
            return self.__team_1
        else:
            return None
