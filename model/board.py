import numpy
import regex

class Board():

    def __init__(self):
        self._size = 15

    def create_board(self):
        self._matrix = numpy.full((self._size, self._size), ' ')

    def insert_play(self, x, y, piece):
        if self.get_value_position(x, y) != ' ':
            return False
        else:
            self.set_value_position(x, y, piece)
            return True

    def check_win(self):
        return False

    def set_value_position(self, x, y, piece):
        self._matrix[x][y] = piece

    def get_value_position(self, x, y):
        return self._matrix[x][y]
    
    def get_size(self):
        return int(self._size)

    def get_matrix(self):
        return self._matrix

    
