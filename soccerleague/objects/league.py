from soccerleague.objects.tournament import Tournament


class League(Tournament):

    def leader_board_output(self, leader_board):
        return [(key, value) for key, value in sorted(leader_board.items(), key=lambda kv: (kv[1], kv[0]),
                                                      reverse=True)]
