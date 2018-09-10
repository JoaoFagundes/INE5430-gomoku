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
        game_over = self._board.check_win()
        while not game_over:
            self.play_turn()
        self._ui.game_over(self.player_in_turn)

    def play_turn(self):
        if self.human_turn():
            self.play_human_turn()
        else:
            self.play_machine_turn()
        self.change_player_turn()

    def play_human_turn(self):
        self._ui.print_board(self._board)
        while True:
            x, y = self._ui.get_human_play(self._board.get_size())
            if self._board.insert_play(x, y, self.player_in_turn):
                break
            self._ui.message_place_occupied()

    def play_machine_turn(self):
        print('Machine played')

    def change_player_turn(self):
        if self.player_in_turn == 'H':
            self.player_in_turn = 'M'
        else:
            self.player_in_turn = 'H'

    def human_turn(self):
        return self.player_in_turn == 'H'

