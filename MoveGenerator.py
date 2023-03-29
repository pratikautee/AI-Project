from copy import copy

class MoveGenerator:
    def __init__(self, input_board_string):
        self.board = input_board_string.split()
        self.numWhitePieces = 0
        self.numBlackPieces = 0
        self.numBlackMoves = 0

    def GenerateMovesOpening(self):
        return self.GenerateAdd()
    
    def GenerateMovesMidgameEndgame(self):
        pass

    def GenerateAdd(self):
        L = list()
        for location, _ in enumerate(self.board):
            if(self.board[location]=='x'):
                b = copy(self.board)
                b[location] = 'W'
                if self.closeMill(location, b):
                    L = self.GenerateRemove(b, L)
                else:
                    L.extend(b)
        return L


    def GenerateHopping(self):
        L = list()
        for location_alpha, _ in enumerate(self.board):
            if(self.board[location_alpha] == "W"):
                for location_beta, _ in enumerate(self.board):
                    if(self.board[location_beta]=='x'):
                        b = copy(self.board)
                        b[location_alpha] = 'x'
                        b[location_beta] = 'W'
                        if (self.closeMill(location_beta, b)):
                            L = self.GenerateRemove(b,L)
                        else:
                            L.extend(b)
        return L


    def GenerateMove(self):
        L = list()
        for location, _ in enumerate(self.board):
            if(self.board[location]=='W'):
                n = self.neighbors(location)
                for j in n:
                    if self.board[j] == 'x':
                        b = copy(self.board)
                        b[location] = 'x'
                        b[j] = 'W'
                        if self.closeMill(j,b):
                            L = self.GenerateRemove(b, L)
                        else:
                            L.extend(b)
        return L

    def GenerateRemove(self, board, L):
        for location,_ in enumerate(board):
            if(board[location]=='B'):
                if( not self.closeMill(location, board)):
                    b = copy(board)
                    b[location] = 'x'
                    L.extend(b)
        if(len(L)==0):
            L.extend(board)
        return L

    def neighbors(self, location):
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
    
    def __comparePieces(self,board, i,j,C):
        return board[i]==C and board[j]==C

    def closeMill(self, location, b):
        C = b[location]
        if(C =='W' or C == 'B'):
            if(location == 0):
                if(self.__comparePieces(b, 1, 2, C) or self.__comparePieces(b, 3, 6, C)):
                    return True
            elif(location == 1):
                if(self.__comparePieces(b, 0, 2, C)):
                    return True
            elif(location == 2):
                if(self.__comparePieces(b, 0, 1, C) or self.__comparePieces(b, 5, 7, C) or self.__comparePieces(b, 12, 21, C)):
                    return True
            elif(location == 3):
                if(self.__comparePieces(b, 0, 6, C) or self.__comparePieces(b, 4, 5, C) or  self.__comparePieces(b, 8, 16, C)):
                    return True
            elif(location == 4):
                if(self.__comparePieces(b, 3,5, C)):
                    return True
            elif(location == 5):
                if(self.__comparePieces(b, 2, 7, C) or self.__comparePieces(b, 3, 4, C) or self.__comparePieces(b, 11, 18)):
                    return True
            elif(location == 6):
                if(self.__comparePieces(b, 0, 3, C) or self.__comparePieces(b, 9, 13, C)):
                    return True
            elif(location == 7):
                if(self.__comparePieces(b, 5, 2, C) or self.__comparePieces(b, 10, 15, C)):
                    return True
            elif(location == 8):
                if(self.__comparePieces(b, 3, 16, C)):
                    return True
            elif(location == 9):
                if(self.__comparePieces(b, 6, 13, C)):
                    return True
            elif(location == 10):
                if(self.__comparePieces(b, 7, 15, C) or self.__comparePieces(b, 11, 12, C)):
                    return True
            elif(location == 11):
                if(self.__comparePieces(b, 10, 12, C) or self.__comparePieces(b, 5, 18, C)):
                    return True
            elif(location == 12):
                if(self.__comparePieces(b, 10, 11, C) or self.__comparePieces(b, 2, 21, C)):
                    return True
            elif(location == 13):
                if(self.__comparePieces(b, 9, 6, C) or self.__comparePieces(b, 16, 19, C) or  self.__comparePieces(b, 14, 15, C)):
                    return True
            elif(location == 14):
                if(self.__comparePieces(b, 13, 15, C) or self.__comparePieces(b, 17, 20, C)):
                    return True
            elif(location == 15):
                if(self.__comparePieces(b, 10, 7, C) or self.__comparePieces(b, 13, 14, C) or  self.__comparePieces(b, 18, 21, C)):
                    return True
            elif(location == 16):
                if(self.__comparePieces(b, 13, 19, C) or self.__comparePieces(b, 3, 8, C) or  self.__comparePieces(b, 17, 18, C)):
                    return True
            elif(location == 17):
                if(self.__comparePieces(b, 14, 20, C) or self.__comparePieces(b, 16, 18, C)):
                    return True
            elif(location == 18):
                if(self.__comparePieces(b, 15, 21, C) or self.__comparePieces(b, 11, 5, C) or  self.__comparePieces(b, 16, 17, C)):
                    return True
            elif(location == 19):
                if(self.__comparePieces(b, 16, 13, C) or self.__comparePieces(b, 20, 21, C)):
                    return True
            elif(location == 20):
                if(self.__comparePieces(b, 19, 21, C) or self.__comparePieces(b, 17, 14, C)):
                    return True
            elif(location == 21):
                if(self.__comparePieces(b, 19, 20, C) or self.__comparePieces(b, 15, 18, C) or  self.__comparePieces(b, 12, 2, C)):
                    return True
        return False

    def staticEstimation(self, b):
        pass
