import sys
from MoveGenerator import MoveGenerator
import math
from utils import flip_pieces

positions_evaluated = 0
output_board_position = []

def MaxMin(x, curr_depth):
    global positions_evaluated, output_board_position
    if(curr_depth>=MAX_DEPTH):
        positions_evaluated+=1
        return MoveGenerator.staticEstimationV2(x)
    else:
        v = -math.inf
        x_children = MoveGenerator.GenerateMovesOpening(x)
        for y in x_children:
            v_res = MinMax(y,curr_depth+1)
            if(v_res>v):
                v = v_res
                output_board_position = y
        return v

def MinMax(x, curr_depth):
    global positions_evaluated
    if(curr_depth>=MAX_DEPTH):
        positions_evaluated+=1
        return MoveGenerator.staticEstimationV2(x)
    else:
        v = math.inf
        x_children = MoveGenerator.GenerateMovesOpening(flip_pieces(x))
        x_children = list(map(lambda x: flip_pieces(x), x_children))
        for y in x_children:
            v_res = MaxMin(y, curr_depth+1)
            if(v_res<v):
                v = v_res
        return v



if __name__ == "__main__":
    MAX_DEPTH = 1
    input_board = open(sys.argv[1]).readline().strip()
    if(sys.argv[3]):
        MAX_DEPTH = int(sys.argv[3])
    estimate = MaxMin(list(input_board), 0)
    
    print(f'Board Position: {"".join(output_board_position)}')
    print(f'Positions evaluated by static estimation: {positions_evaluated}.')
    print(f'MINIMAX estimate: {estimate}')

    with open(sys.argv[2], 'w') as output_board:
        output_board.write("".join(output_board_position))

