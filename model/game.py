from model.board import Board
from ui.userInterface import UserInterface

class Game():

    def __init__(self):
        self.board = Board()
        self.ui = UserInterface()


    def start_game(self):
        self.board.create_board()
        self.ui.print_board(self.board)
