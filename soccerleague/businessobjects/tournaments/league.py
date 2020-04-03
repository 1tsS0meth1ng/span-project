from soccerleague.businessobjects.tournaments.tournament import Tournament


class League(Tournament):
    """ A league class specialization of the tournament class

    """

    def increment_score(self, winner, loser, match):
        if winner is not None:
            if self._leader_board.get(winner) is None:
                self._leader_board[winner] = 3
            else:
                self._leader_board[winner] += 3

            if self._leader_board.get(loser) is None:
                self._leader_board[loser] = 0
        else:

            if self._leader_board.get(match.team_1) is None:
                self._leader_board[match.team_1] = 1
            else:
                self._leader_board[match.team_1] += 1

            if self._leader_board.get(match.team_2) is None:
                self._leader_board[match.team_2] = 1
            else:
                self._leader_board[match.team_2] += 1

    def leader_board_output(self, leader_board):
        return [(key, value) for key, value in sorted(leader_board.items(), key=lambda kv: (kv[1], kv[0]),
                                                      reverse=True)]
