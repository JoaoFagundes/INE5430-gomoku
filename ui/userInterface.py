from model.board import Board

class UserInterface():

    def print_board(self, board):
        matrix = board.get_matrix()

        # Printing an number above each column for identification
        column_id = str('   ')
        for j in range(board.get_size()):
            if j < 10:
                column_id += ' ' + str(j) + ' '
            else:
                column_id += str(j) + ' '

        print(column_id)

        # Printing the whole board
        for i in range(board.get_size()):
            row = str(i) + ' '
            if i < 10:
                row += ' '
            for j in range(board.get_size()):
                row += '[' + matrix[i][j] + ']'
            
            print(row)


    def get_first_player(self):
        while (True):
            first_player = input("Please, insert who will make the first play ('H' for human, 'M' for machine): ").upper()
            if (first_player in {'M', 'H'}):
                return first_player
            else:
                print('You entered an invalid value.')

    def get_human_play(self, size):
        while (True):
            print("Considering the numbers on the left of each line and on top of each column, make your play")
            try:
                position = input("Please, insert the line and column value separated by commas (e.g. 0, 0): ").split(',')
                x = int(position[0])
                y = int(position[1])
                if x not in range(size) or y not in range(size):
                    print("You entered an invalid value.")
                else:
                    return x, y
            except ValueError:
                print('\n\nPlease insert two valid values separated by comma.')
    
    def message_place_occupied(self):
        print('\n\nThe place chosen is already occupied by some piece')

    def game_over(self, player):
        if player == 'H':
            print("\n\nWell done, you won the game. I'll start improving my AI right away.")
        else:
            print("\n\nToo bad (for you), you lost the game. Better luck next time")
