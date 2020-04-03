from soccerleague import SoccerTeam, SoccerMatch, Tournament


class TournamentView:

    def __init__(self, tournament):
        self._tournament: Tournament = tournament
        self.__run = True
        self._options = {
            1: self.import_matches,
            2: self.view_leader_board,
            3: self.quit_interface
        }

    def run(self):
        print(f'Welcome to {self._tournament.tournament_name}\'s page')
        while self.__run:
            print('1. Import matches')
            print('2. View Leader Board')
            print('3. Go back')

            try:
                selection = int(input('Input the number of the menu item which you would like to interact with: '))
                function = self._options.get(selection)
                if function:
                    function()
                else:
                    print('invalid input')

            except ValueError:
                print('Invalid Input')
            print('------------------------------------------------------')

    def quit_interface(self):
        self.__run = False

    def import_matches(self):
        directory = input('input the directory of the match file: ')
        directory = directory.strip()
        try:
            with open(directory) as f:
                lines = f.readlines()
                for line in lines:

                    line = line.replace('\n', '')
                    team_scores = line.split(',')

                    teams = []
                    scores = []
                    for team_score in team_scores:
                        split_name_score = team_score.split(' ')
                        score = int(split_name_score[-1])
                        scores.append(score)
                        name = ' '
                        name = name.join(split_name_score[:-1])
                        name = name.strip()
                        teams.append(SoccerTeam(name))

                    self._tournament.add_match(SoccerMatch(teams[0], scores[0], teams[-1], scores[-1]))
                    scores.clear()
                    teams.clear()
            print('Successfully added!')
        except FileNotFoundError:
            print('The given file cannot be accessed')

    def view_leader_board(self):
        print('Leader Board:')
        name_list = [(value[0].competitor_name, value[-1]) for value in self._tournament.leader_board]
        for index, name_score in enumerate(name_list):
            print(f'{index + 1}. {name_score[0]} {name_score[-1]} pts')
