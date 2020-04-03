class SoccerTeam:
    """ An object which represents a soccer team
    """

    __team_name: str = None

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
    def team_name(self) -> str:
        """team_name: str object which represents the team's name

        The setter checks if the correct type str is being set else it raises a TypeError
        """
        return self.__team_name

    @team_name.setter
    def team_name(self, team_name: str):
        if type(team_name) is str:
            self.__team_name = team_name
        else:
            raise TypeError('Team name needs to be of type str')

    def __lt__(self, other):
        if self.team_name < other.team_name:
            return True
        else:
            return False
