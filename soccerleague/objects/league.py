from typing import Collection
from soccerleague.objects.match import Match


class League:
    __league_name: str = None
    __matches: Collection[Match] = []

    def __init__(self, name):
        self.league_name = name

    @property
    def league_name(self):
        return self.__league_name

    @league_name.setter
    def league_name(self, value):
        if type(value) is str:
            if value != '':
                self.__league_name = value
            else:
                raise ValueError('League name cannot be an empty string')
        else:
            raise TypeError('League name needs to be of type str')

    @property
    def matches(self) -> Collection[Match]:
        pass
