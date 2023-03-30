import sys
from MoveGenerator import MoveGenerator
import math

from utils import flip_pieces

positions_evaluated = 0
output_board_position = []

def MaxMin(x, curr_depth, alpha, beta):
    global positions_evaluated, output_board_position
    if(curr_depth>=MAX_DEPTH):
        positions_evaluated+=1
        return MoveGenerator.staticEstimation(x, mode='midgame_endgame')
    else:
        d = curr_depth+1
        v = -math.inf
        x_children = MoveGenerator.GenerateMovesMidgameEndgame(x)
        output_board_position = x_children[0]
        for y in x_children:
            v = max(v, MinMax(y, d, alpha, beta))
            if (v >= beta):
                return v
            else:
                alpha = max(v, alpha)
        return v

def MinMax(x, curr_depth, alpha, beta):
    global positions_evaluated, output_board_position
    if(curr_depth>=MAX_DEPTH):
        positions_evaluated+=1
        return MoveGenerator.staticEstimation(x, mode='midgame_endgame')
    else:
        d = curr_depth+1
        v = math.inf
        x_children = MoveGenerator.GenerateMovesMidgameEndgame(flip_pieces(x))
        x_children = list(map(lambda x: flip_pieces(x), x_children))
        output_board_position = x_children[0]
        for y in x_children:
            v = min(v, MaxMin(y, d, alpha, beta))
            if(v<=alpha):
                return v
            else:
                beta = min(v, beta)
        return v



if __name__ == "__main__":
    MAX_DEPTH = 1
    input_board = open(sys.argv[1]).readline().strip()
    if(sys.argv[3]):
        MAX_DEPTH = int(sys.argv[3])
    estimate = MaxMin(list(input_board), 0, alpha=-math.inf, beta=math.inf)
    print(f'Board Position: {"".join(output_board_position)}')
    print(f'Positions evaluated by static estimation: {positions_evaluated}.')
    print(f'MINIMAX estimate: {estimate}')

