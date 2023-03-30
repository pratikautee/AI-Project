def flip_pieces(board):
    flip_dict = {
                'W': 'B',
                'B': 'W',
                'x': 'x'
            }
    return list(map(lambda x: flip_dict[x], board))