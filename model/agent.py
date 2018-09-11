from math import inf

def play(board):
    score, x, y = compute_max(board)
    board.insert_play(x, y, 'M')

def compute_max(board):
    best_score = -inf
    x, y = 0, 0
    board_size = board.get_size()
    for i in range(board_size):
        for j in range(board_size):
            if not board.insert_play(i, j, 'M'):
                continue
            play_score = compute_min(board)
            if play_score > best_score:
                best_score = play_score
                x, y = i, j
            board.set_value_position(i, j, ' ')
    return best_score, x, y

def compute_min(board):
    best_score = inf
    board_size = board.get_size()
    for i in range(board_size):
        for j in range(board_size):
            if not board.insert_play(i, j, 'H'):
                continue
            play_score, x, y = compute_max(board)
            if play_score > best_score:
                best_score = play_score
            board.set_value_position(i, j, ' ')
    return best_score
