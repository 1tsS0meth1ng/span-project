class SoccerTeam:
    """
    Attributes
    ----------
    team_name : str
        Name of the team which the object is describing
    """
    def __init__(self, team_name: str):
        """Init of the SoccerTeam class

        Initializes the SoccerTeam by giving the object a name.

        Parameters
        ----------
        team_name : str
            The teams name
        """
        self.team_name = team_name

    @property
    def team_name(self):
        return self.__team_name

    @team_name.setter
    def team_name(self, team_name):
        if type(team_name) is str:
            self.__team_name = team_name
        else:
            raise TypeError

    @team_name.getter
    def team_name(self):
        return self.__team_name
