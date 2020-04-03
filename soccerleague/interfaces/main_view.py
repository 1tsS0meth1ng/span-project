from soccerleague import League
from soccerleague.interfaces.tournament_view import TournamentView


class MainView:

    def __init__(self):
        self.__tournament_dict: dict = {}
        self.__run = True
        self._options: dict = {
            1: self.view_tournaments,
            2: self.add_league,
            3: self.view_league,
            4: self.quit_interface
        }

    def view_tournaments(self):
        output = ''
        for k in self.__tournament_dict:
            output += k + '\n'

        if len(output) == 0:
            output = 'No tournaments registered'
        else:
            output = output[:-1]
            output = "Tournaments:\n" + output

        print(output)

    def add_league(self):
        tournament_name = input('Give the league a name: ')
        if self.__tournament_dict.get(tournament_name):
            print('That name has already been taken')
        else:
            self.__tournament_dict[tournament_name] = League(tournament_name)
            print(f'{tournament_name} has been successfully registered')

    def view_league(self):
        tournament_name = input('input tournament name: ')
        tournament = self.__tournament_dict.get(tournament_name)
        if tournament:
            tv = TournamentView(tournament)
            tv.run()
        else:
            print('Invalid tournament name')

    def quit_interface(self):
        self.__run = False

    def run(self):
        print('Welcome the the league manager')
        while self.__run:
            print('1. View a list of the current leagues')
            print('2. Add a league')
            print('3. View a select league')
            print('4. Quit')
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
