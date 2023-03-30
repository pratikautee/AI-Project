import sys
import MiniMaxGame


if __name__ == "__main__":
    flip_dict = {
                'W': 'B',
                'B': 'W',
                'x': 'x'
            }
    MiniMaxGame.MAX_DEPTH = 1

    input_board = open(sys.argv[1]).readline().strip()
    flipped_board = list(map(lambda x: flip_dict[x], list(input_board)))

    if(sys.argv[3]):
        MiniMaxGame.MAX_DEPTH = int(sys.argv[3])

    estimate = MiniMaxGame.MaxMin(list(flipped_board), 0)
    output_board_position_flipped = list(map(lambda x: flip_dict[x], list(MiniMaxGame.output_board_position)))
    
    print(f'Board Position: {"".join(output_board_position_flipped)}')
    print(f'Positions evaluated by static estimation: {MiniMaxGame.positions_evaluated}.')
    print(f'MINIMAX estimate: {estimate}')