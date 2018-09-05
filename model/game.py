from model.board import Board
from ui.userInterface import UserInterface

class Game():

    def __init__(self):
        self._board = Board()
        self._ui = UserInterface()


    def start_game(self):
        self._board.create_board()
        self.player_in_turn = self._ui.get_first_player()
        self.play_game()

    def play_game(self):
        game_on = True
        while(game_on):
            if self.human_turn():
                self._ui.print_board(self._board)
                while True:
                    x, y = self._ui.get_human_play(self._board.get_size())
                    if not self._board.insert_play(x, y, self.player_in_turn):
                        self._ui.message_place_occupied()
                        continue
                    else:
                        break
            else:
                print("Machine played")

            if self._board.check_win():
                self._ui.print_board(self._board)
                self._ui.game_over(self.player_in_turn)
                break
            
            self.change_player_turn()

                


    def change_player_turn(self):
        if self.player_in_turn == 'H':
            self.player_in_turn = 'M'
        else:
            self.player_in_turn = 'H'

    def human_turn(self):
        return self.player_in_turn == 'H'

