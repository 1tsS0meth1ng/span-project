from soccerleague.businessobjects.competitors.team import Team


class SoccerTeam(Team):
    """ A specialization of Team used to represent a soccer team
    """

    def __lt__(self, other: "SoccerTeam"):
        """
        Parameters
        ----------
        other : SoccerTeam
            The soccer team which is being compared to this soccer team

        Returns
        -------
        bool
            Returns True if this soccer team's name is < the other team, Else returns False

        """
        if self.competitor_name < other.competitor_name:
            return True
        else:
            return False
