"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player

# Add your functions here.
print(provided.EMPTY)


def mc_trial(board, player):
    empty = board.get_empty_squares()
    random_sqr = random.choice(empty)
    board.move(random_sqr[0], random_sqr[1], player)
    player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    win = board.check_win()
    for r in range(board.get_dim()):
        for c in range(board.get_dim()):
            cell = board.square(r, c)
            if cell == provided.PLAYERX and win == provided.PLAYERX:
                scores[r][c] += SCORE_CURRENT
            elif cell == provided.PLAYERO and win == provided.PLAYERO:
                scores[r][c] -= SCORE_OTHER
            elif cell == provided.PLAYERX and win == provided.PLAYERO:
                scores[r][c] -= SCORE_OTHER
            elif cell == provided.PLAYERO and win == provided.PLAYERX:
                scores[r][c] += SCORE_CURRENT
    print(scores)


def get_best_move(board, scores):
    empty = board.get_empty_squares()
    max_value = 0
    h_s = []
    for r in range(board.get_dim()):
        for c in range(board.get_dim()):
            cell = (r, c)
            if scores[r][c] > max_value and cell in empty:
                max_value = scores[r][c]
                h_s.append(scores[r][c])
            elif scores[r][c] == max_value and cell in empty:
                max_value = scores[r][c]
                h_s.append(scores[r][c])

    random.choice(h_s)
    return h_s


def mc_move(board, player, trials):
    zero_sqr = [[0 for i in range(board.get_dim())] for k in range(board.get_dim())]

    for i in range(trials):
        clone_b = board.clone()
        mc_trial(clone_b, player)
        mc_update_scores(zero_sqr, clone_b, player)

    b_move = get_best_move(board, zero_sqr)
    return b_move


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
