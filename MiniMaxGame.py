import sys
from MoveGenerator import MoveGenerator
import math

positions_evaluated = 0
output_board_position = []

def MaxMin(x, curr_depth):
    global positions_evaluated, output_board_position
    if(curr_depth>=MAX_DEPTH):
        positions_evaluated+=1
        return MoveGenerator.staticEstimation(x, mode='midgame_endgame')
    else:
        v = -math.inf
        x_children = MoveGenerator.GenerateMovesMidgameEndgame(x)
        output_board_position = x_children[0]
        for y in x_children:
            v = max(v, MinMax(y, curr_depth+1))
        return v

def MinMax(x, curr_depth):
    global positions_evaluated, output_board_position
    if(curr_depth>=MAX_DEPTH):
        positions_evaluated+=1
        return MoveGenerator.staticEstimation(x, mode='midgame_endgame')
    else:
        v = math.inf
        x_children = MoveGenerator.GenerateMovesMidgameEndgame(x)
        output_board_position = x_children[0]
        for y in x_children:
            v = min(v, MaxMin(y, curr_depth+1))
        return v



if __name__ == "__main__":
    MAX_DEPTH = 1
    input_board = open(sys.argv[1]).readline().strip()
    if(sys.argv[3]):
        MAX_DEPTH = int(sys.argv[3])
    estimate = MaxMin(list(input_board), 0)
    print(f'Board Position: {"".join(output_board_position)}')
    print(f'Positions evaluated by static estimation: {positions_evaluated}.')
    print(f'MINIMAX Opening estimate: {estimate}')

