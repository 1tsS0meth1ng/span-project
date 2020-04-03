from soccerleague.businessobjects.competitors.competitor import Competitor


class Team(Competitor):
    """ A specialization of Competitor used to represent a team
    """

    def __hash__(self):
        pass

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        if self.competitor_name == other.competitor_name:
            return True
        else:
            return False
