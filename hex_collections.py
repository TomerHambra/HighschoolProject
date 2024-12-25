import json
import emoji


SIZE = 7
red_block = emoji.emojize(':red_square:')
blue_block = emoji.emojize(':blue_square:')
white_block = emoji.emojize(':white_large_square:')


def to_char(val):
    return red_block if val == '2' else blue_block if val == '0' else white_block


def print_board(board):
    pref = ''
    for i in range(SIZE):
        print(pref, end='')
        pref += ' '
        for j in range(SIZE):
            print(to_char(board[i*SIZE+j]), end=' ')
        print()


def print_boards_list(boards_list, path=''):
    bank = {}
    if path != '':
        with open(path, 'r') as f:
            bank = json.load(f)
    for board, rank in boards_list:
        print_board(board)
        if path != '':
            rank = bank.get(board)
            rank = rank[0] if rank else '?'
        print('Evaluation: '+str(rank))
        print()
