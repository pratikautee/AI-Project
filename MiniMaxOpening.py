import sys
import os

if __name__ == "__main__":
    input_file = open(sys.argv[1])
    input_board = input_file.readline().strip()
    with open(sys.argv[2], 'w') as f:
        f.write('WxWWxWWWWBBBBBBBBxxxxx')