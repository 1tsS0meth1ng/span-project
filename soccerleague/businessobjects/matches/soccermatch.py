import uuid
from typing import Optional

from soccerleague.businessobjects.competitors.competitor import Competitor
from soccerleague.businessobjects.matches.match import Match


class SoccerMatch(Match):
    """ A match with both soccer teams and both soccer teams scores

    """

    def get_winner(self) -> Optional[Competitor]:
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
        difference = self.team_1_score - self.team_2_score

        if difference > 0:
            return self.team_1
        elif difference < 0:
            return self.team_2
        else:
            return None

    def get_loser(self) -> Optional[Competitor]:
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
        difference = self.team_1_score - self.team_2_score

        if difference > 0:
            return self.team_2
        elif difference < 0:
            return self.team_1
        else:
            return None

    def __hash__(self):
        return hash(self.__repr__())
