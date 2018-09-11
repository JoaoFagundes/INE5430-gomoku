import numpy as np
import copy
from math import inf
from random import randint

def play(board):
    score, x, y = minimax(board, 'M', -inf, inf, 1)
    board.insert_play(x, y, 'M')

def minimax(board, player, alpha, beta, level):
    if level == 3 or board.check_win():
        return int(randint(-50, 50)), None, None
    
    best_play = None
    for play in every_possible_play(board):
        if player == 'M':
            board.set_value_position(play[0], play[1], 'M')
            score = minimax(board, 'H', alpha, beta, level + 1)[0]
            board.set_value_position(play[0], play[1], ' ')
            
            if score > alpha:
                best_play = play
                alpha = score
            if alpha >= beta:
                return alpha, best_play[0], best_play[1]
        else:
            board.set_value_position(play[0], play[1], 'H')
            score = minimax(board, 'M', alpha, beta, level + 1)[0]
            board.set_value_position(play[0], play[1], ' ')

            if score < beta:
                best_play = play
                beta = score
            if beta <= alpha:
                return beta, best_play[0], best_play[1]
        
    if player == 'M':
        return alpha, best_play[0], best_play[1]
    else:
        return beta, best_play[0], best_play[1]

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

def every_possible_play(board):
    possible_plays = list()
    while True:
        i, j = best_available_play(board)
        if i == None or j == None:
            break
        board.set_value_position(i, j, 'X')
        possible_plays.append((i, j))
    
    for move in possible_plays:
        board.set_value_position(move[0], move[1], ' ')

    return possible_plays


