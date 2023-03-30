from copy import copy
from utils import flip_pieces
class MoveGenerator:
   
    @staticmethod
    def GenerateMovesOpening(board):
        return MoveGenerator.GenerateAdd(board)
    
    @staticmethod
    def GenerateMovesMidgameEndgame(board):
        L = list()
        if(board.count('W') == 3):
            return MoveGenerator.GenerateHopping(board)
        else:
            return MoveGenerator.GenerateMove(board)

    @staticmethod
    def GenerateAdd(board):
        L = list()
        for location, _ in enumerate(board):
            if(board[location]=='x'):
                b = copy(board)
                b[location] = 'W'
                if MoveGenerator.closeMill(location, b):
                    L = MoveGenerator.GenerateRemove(b, L)
                else:
                    L.append(b)
        return L

    @staticmethod
    def GenerateHopping(board):
        L = list()
        for location_alpha, _ in enumerate(board):
            if(board[location_alpha] == "W"):
                for location_beta, _ in enumerate(board):
                    if(board[location_beta]=='x'):
                        b = copy(board)
                        b[location_alpha] = 'x'
                        b[location_beta] = 'W'
                        if (MoveGenerator.closeMill(location_beta, b)):
                            L = MoveGenerator.GenerateRemove(b,L)
                        else:
                            L.append(b)
        return L

    @staticmethod
    def GenerateMove(board):
        L = list()
        for location, _ in enumerate(board):
            if(board[location]=='W'):
                n = MoveGenerator.neighbors(location)
                for j in n:
                    if board[j] == 'x':
                        b = copy(board)
                        b[location] = 'x'
                        b[j] = 'W'
                        if MoveGenerator.closeMill(j,b):
                            L = MoveGenerator.GenerateRemove(b, L)
                        else:
                            L.append(b)
        return L
    
    @staticmethod
    def GenerateRemove(board, L):
        L_copy = copy(L)
        positionAddedFlag = False
        for location,_ in enumerate(board):
            if(board[location]=='B'):
                if(MoveGenerator.closeMill(location, board) == False):
                    b = copy(board)
                    b[location] = 'x'
                    L_copy.append(b)
                    positionAddedFlag = True
        if(positionAddedFlag == False):
            L_copy.append(board)
        return L_copy

    @staticmethod
    def neighbors(location):
        neighbors_dict = {
            0: [19, 3, 1],
            1: [0, 4, 2],
            2: [1, 5, 12],
            3: [0, 8, 6, 4],
            4: [3, 1, 5],
            5: [4, 7, 11, 2],
            6: [3, 9, 7],
            7: [6, 10, 5],
            8: [3, 16, 9],
            9: [8, 6, 13],
            10: [7, 15, 11],
            11: [10, 5, 18, 12],
            12: [11, 2, 21],
            13: [16, 9, 14],
            14: [13, 17, 15],
            15: [14, 10, 18],
            16: [19, 8, 13, 17],
            17: [16, 14, 20, 18],
            18: [17, 15, 11, 21],
            19: [0, 16, 20],
            20: [19, 17, 21],
            21: [20, 18, 12]
        }

        return neighbors_dict[location]
    
    @staticmethod
    def __comparePieces(board, i,j,C):
        return board[i]==C and board[j]==C
    
    @staticmethod
    def closeMill(location, b):
        C = b[location]
        if(C =='W' or C == 'B'):
            if(location == 0):
                if(MoveGenerator.__comparePieces(b, 1, 2, C) or MoveGenerator.__comparePieces(b, 3, 6, C)):
                    return True
            elif(location == 1):
                if(MoveGenerator.__comparePieces(b, 0, 2, C)):
                    return True
            elif(location == 2):
                if(MoveGenerator.__comparePieces(b, 0, 1, C) or MoveGenerator.__comparePieces(b, 5, 7, C) or MoveGenerator.__comparePieces(b, 12, 21, C)):
                    return True
            elif(location == 3):
                if(MoveGenerator.__comparePieces(b, 0, 6, C) or MoveGenerator.__comparePieces(b, 4, 5, C) or  MoveGenerator.__comparePieces(b, 8, 16, C)):
                    return True
            elif(location == 4):
                if(MoveGenerator.__comparePieces(b, 3,5, C)):
                    return True
            elif(location == 5):
                if(MoveGenerator.__comparePieces(b, 2, 7, C) or MoveGenerator.__comparePieces(b, 3, 4, C) or MoveGenerator.__comparePieces(b, 11, 18, C)):
                    return True
            elif(location == 6):
                if(MoveGenerator.__comparePieces(b, 0, 3, C) or MoveGenerator.__comparePieces(b, 9, 13, C)):
                    return True
            elif(location == 7):
                if(MoveGenerator.__comparePieces(b, 5, 2, C) or MoveGenerator.__comparePieces(b, 10, 15, C)):
                    return True
            elif(location == 8):
                if(MoveGenerator.__comparePieces(b, 3, 16, C)):
                    return True
            elif(location == 9):
                if(MoveGenerator.__comparePieces(b, 6, 13, C)):
                    return True
            elif(location == 10):
                if(MoveGenerator.__comparePieces(b, 7, 15, C) or MoveGenerator.__comparePieces(b, 11, 12, C)):
                    return True
            elif(location == 11):
                if(MoveGenerator.__comparePieces(b, 10, 12, C) or MoveGenerator.__comparePieces(b, 5, 18, C)):
                    return True
            elif(location == 12):
                if(MoveGenerator.__comparePieces(b, 10, 11, C) or MoveGenerator.__comparePieces(b, 2, 21, C)):
                    return True
            elif(location == 13):
                if(MoveGenerator.__comparePieces(b, 9, 6, C) or MoveGenerator.__comparePieces(b, 16, 19, C) or  MoveGenerator.__comparePieces(b, 14, 15, C)):
                    return True
            elif(location == 14):
                if(MoveGenerator.__comparePieces(b, 13, 15, C) or MoveGenerator.__comparePieces(b, 17, 20, C)):
                    return True
            elif(location == 15):
                if(MoveGenerator.__comparePieces(b, 10, 7, C) or MoveGenerator.__comparePieces(b, 13, 14, C) or  MoveGenerator.__comparePieces(b, 18, 21, C)):
                    return True
            elif(location == 16):
                if(MoveGenerator.__comparePieces(b, 13, 19, C) or MoveGenerator.__comparePieces(b, 3, 8, C) or  MoveGenerator.__comparePieces(b, 17, 18, C)):
                    return True
            elif(location == 17):
                if(MoveGenerator.__comparePieces(b, 14, 20, C) or MoveGenerator.__comparePieces(b, 16, 18, C)):
                    return True
            elif(location == 18):
                if(MoveGenerator.__comparePieces(b, 15, 21, C) or MoveGenerator.__comparePieces(b, 11, 5, C) or  MoveGenerator.__comparePieces(b, 16, 17, C)):
                    return True
            elif(location == 19):
                if(MoveGenerator.__comparePieces(b, 16, 13, C) or MoveGenerator.__comparePieces(b, 20, 21, C)):
                    return True
            elif(location == 20):
                if(MoveGenerator.__comparePieces(b, 19, 21, C) or MoveGenerator.__comparePieces(b, 17, 14, C)):
                    return True
            elif(location == 21):
                if(MoveGenerator.__comparePieces(b, 19, 20, C) or MoveGenerator.__comparePieces(b, 15, 18, C) or  MoveGenerator.__comparePieces(b, 12, 2, C)):
                    return True
        return False
    
    @staticmethod
    def __getNumBlackMoves(b):
        b_copy = flip_pieces(b)
        L = MoveGenerator.GenerateMovesMidgameEndgame(b_copy)
        return len(L)

    @staticmethod
    def staticEstimation(b, mode='opening'):
        numWhitePieces = b.count('W')
        numBlackPieces = b.count('B')
        if(mode=='midgame_endgame'):
            numBlackMoves = MoveGenerator.__getNumBlackMoves(b)
            if(numBlackPieces<=2):
                return 10_000
            elif (numWhitePieces <= 2):
                return -10_000
            elif(numBlackMoves==0):
                return 10_000
            else:
                return (1000*(numWhitePieces - numBlackPieces) - numBlackMoves)
            
        elif(mode == 'opening'):
            return (numWhitePieces - numBlackPieces)
