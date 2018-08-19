# Joao Victor Fagundes
# Salomao Rodrigues Jacinto
# INE5421 - Trabalho Prático I Junho 2018

import json
from collections import OrderedDict

class Board():

    def __init__(self):
        self.num_rows = 15
        self.num_columns = 15 

    def create_board(self):
        self.matrix = [' '] * self.num_rows
        for i in range(self.num_rows):
            self.matrix[i] = [' '] * self.num_columns

    def get_num_rows(self):
        return self.num_rows

    def get_num_columns(self):
        return self.num_columns

    def get_matrix(self):
        return self.matrix
