import sys
import MiniMaxOpening
from utils import flip_pieces

if __name__ == "__main__":
    MiniMaxOpening.MAX_DEPTH = 1

    input_board = open(sys.argv[1]).readline().strip()
    flipped_board = flip_pieces(list(input_board))

    if(sys.argv[3]):
        MiniMaxOpening.MAX_DEPTH = int(sys.argv[3])

    estimate = MiniMaxOpening.MaxMin(list(flipped_board), 0)
    output_board_position_flipped = flip_pieces(MiniMaxOpening.output_board_position)  

    print(f'Board Position: {"".join(output_board_position_flipped)}')
    print(f'Positions evaluated by static estimation: {MiniMaxOpening.positions_evaluated}.')
    print(f'MINIMAX estimate: {estimate}')

    with open(sys.argv[2], 'w') as output_board:
        output_board.write("".join(output_board_position_flipped))