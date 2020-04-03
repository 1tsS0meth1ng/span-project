from abc import ABC, abstractmethod


class Competitor(ABC):
    """ A class which represents a competitor
    Attributes
    ----------
     __competitor_name : str
        The competitor's name
    """

    def __init__(self, competitor_name: str):
        """Init of the Competitor class

        Initializes the Competitor by giving the object a name.

        Parameters
        ----------
        competitor_name : str
            The competitor's name
        """
        __competitor_name: str = None
        self.competitor_name = competitor_name

    @property
    def competitor_name(self) -> str:
        """competitor_name: str object which represents the competitor's name

        The setter checks if the correct type str is being set else it raises a TypeError
        """
        return self.__competitor_name

    @competitor_name.setter
    def competitor_name(self, competitor_name: str):
        if type(competitor_name) is str:
            self.__competitor_name = competitor_name
        else:
            raise TypeError('Team name needs to be of type str')

    @abstractmethod
    def __lt__(self, other):
        pass
