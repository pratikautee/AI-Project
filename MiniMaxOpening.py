import sys
import os
from MoveGenerator import MoveGenerator
import math

def MaxMin(x, curr_depth):
    if(curr_depth>=MAX_DEPTH):
        global positions_evaluated
        positions_evaluated+=1
        return MoveGenerator.staticEstimation(x)
    else:
        d = curr_depth+1
        v = -math.inf
        x_children = MoveGenerator.GenerateMovesOpening(x)
        global output_board_position
        output_board_position = x_children[0]
        for y in x_children:
            v = max(v, MinMax(y, d))
        return v

def MinMax(x, curr_depth):
    if(curr_depth>=MAX_DEPTH):
        global positions_evaluated
        positions_evaluated+=1
        return MoveGenerator.staticEstimation(x)
    else:
        d = curr_depth+1
        v = math.inf
        x_children = MoveGenerator.GenerateMovesOpening(x)
        global output_board_position
        output_board_position = x_children[0]
        for y in x_children:
            v = min(v, MaxMin(y, d))
        return v



if __name__ == "__main__":
    positions_evaluated = 0
    output_board_position = []
    MAX_DEPTH = 2
    input_board = open(sys.argv[1]).readline().strip()
    if(sys.argv[3]):
        MAX_DEPTH = int(sys.argv[3])
    estimate = MaxMin(list(input_board), 0)

print(f'Board Position: {"".join(output_board_position)}')
print(f'Positions evaluated by static estimation: {positions_evaluated}.')
print(f'MINIMAX Opening estimate: {estimate}')

