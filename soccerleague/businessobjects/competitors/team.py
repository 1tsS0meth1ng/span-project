from soccerleague.businessobjects.competitor.competitor import Competitor


class Team(Competitor):
    """ A abstraction of Competitor used to represent a team
    """
    def __lt__(self, other):
        pass

