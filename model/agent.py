import numpy as np
from math import inf
from random import randint

def play(board):
    score, x, y = compute_max(board, int(1))
    board.insert_play(x, y, 'M')

def compute_max(board, level):
    best_score = -inf
    x, y = 0, 0
    i, j = best_available_play(board)
    if i != None and j != None:
        if (level < 7):
            board.insert_play(i, j, 'M')
            play_score = compute_min(board, level + 1)
            if play_score > best_score:
                best_score = play_score
                x, y = i, j
            board.set_value_position(i, j, ' ')
        else:
            #chama heuristica ou utilidade
            best_score = int(randint(-50, 50))
    return best_score, x, y

def compute_min(board, level):
    best_score = inf
    i, j = best_available_play(board)
    if i != None and j != None:
        if (level < 7):
            board.insert_play(i, j, 'H')
            play_score, x, y = compute_max(board, level + 1)
            if play_score > best_score:
                best_score = play_score
            board.set_value_position(i, j, ' ')
        else:
            #chama heuristica ou utilidade
            best_score = int(randint(-50, 50))

    return best_score

def best_available_play(board):
    board_size = board.get_size()
    
    if board_size % 2 != 0:
        row_range = [int((board_size - 1) / 2)] * 2
    else:
        row_range = [int(board_size / 2)] * 2

    column_range = row_range

    while True:
        for i in range(row_range[0], row_range[1] + 1):
            for j in range(column_range[0], column_range[1] + 1):
                if board.get_value_position(i, j) == ' ':
                    return i, j
        
        if (row_range[0] > 0 and row_range[1] < board_size):
            row_range[0] -= 1
            row_range[1] += 1
            column_range = row_range
        else:
            return None, None



