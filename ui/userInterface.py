from model.board import Board

class UserInterface():

    def print_board(self, board):
        matrix = board.get_matrix()
        for i in range(board.get_num_rows()):
            row = str('')
            for j in range(board.get_num_columns()):
                row += '[' + matrix[i][j] + ']'
            print(row)
        