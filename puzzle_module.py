import random
from enum import Enum

class move(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

CORRECT_POS = ([1,1],[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]) 
# this is for a correct final grid of 
# 1 2 3
# 4 X 5
# 6 7 8

class puzzle_o_eight:
    def __init__(self, other = None):
        if other is None:
            self.matr: list[list[int]] = [[0 for _ in range(3)] for _ in range(3)]
            num = 0
            for i in range(3):
                for j in range (3):
                    self.matr[i][j] = num
                    num = num + 1
            self.blank_pos = [0,0]
        else:
            self.matr = [row[:] for row in other.matr]
            self.blank_pos = other.blank_pos[:]
    
    def __repr__(self):
        ret = ""
        for i in range(3):
            for j in range (3):
                if (self.matr[i][j] == 0):
                    ret += '█' + ' '
                else:
                    ret += str(self.matr[i][j]) + ' '
            
            ret += '\n'
        return ret
    def self_random_shuffle(self, shuf_iter):
        for iteration in range(shuf_iter): # yes one hundred whole times
            ra = random.randint(0, 2)
            ca = random.randint(0, 2)

            rb = random.randint(0, 2)
            cb = random.randint(0, 2)
            # grab random points to swap between

            self.matr[ra][ca], self.matr[rb][cb] = self.matr[rb][cb], self.matr[ra][ca] # swap
        

        for i in range(3):
            for j in range(3):
                if(self.matr[i][j] == 0):
                    self.blank_pos = [i, j]
                    break

    def heuristics(self): # based on sum of manhattan distances of each tile away from where they should be in the final config
        hrt_sum = 0
        for i in range(3):
            for j in range(3):
                if(self.matr[i][j] == 0): # if blank tile then skip
                    continue
                cur_hrt = abs(i - CORRECT_POS[self.matr[i][j]][0]) + abs(j - CORRECT_POS[self.matr[i][j]][1])
                hrt_sum += cur_hrt
        return hrt_sum
    
    def get_possible_move(self):
        ret = [] # left, up, right, down
        r_mod = [0,-1,0,1]
        c_mod = [-1,0,1,0]
        moves = [move.LEFT, move.UP, move.RIGHT, move.DOWN]

        for i in range(4):
            new_pos = [self.blank_pos[0] + r_mod[i], self.blank_pos[1] + c_mod[i]]
            if(new_pos[0] < 0 or new_pos[0] >= 3 or new_pos[1] < 0 or new_pos[1] >= 3):
                continue
            ret.append(moves[i])
        return ret
    
    def move_ret_anew(self, mv):
        r_mod = [0,-1,0,1]
        c_mod = [-1,0,1,0]

        sacrificial = puzzle_o_eight(self) # avoids changing the original

        move_tile = [sacrificial.blank_pos[0] + r_mod[mv.value], sacrificial.blank_pos[1] + c_mod[mv.value]]
        if(move_tile[0] < 0 or move_tile[0] >= 3 or move_tile[1] < 0 or move_tile[1] >= 3): # invald position
            raise Exception("Illegal move")
        
        sacrificial.matr[sacrificial.blank_pos[0]][sacrificial.blank_pos[1]], sacrificial.matr[move_tile[0]][move_tile[1]] = sacrificial.matr[move_tile[0]][move_tile[1]], sacrificial.matr[sacrificial.blank_pos[0]][sacrificial.blank_pos[1]]
        sacrificial.blank_pos = [move_tile[0], move_tile[1]]
        return sacrificial
    
    def __self_move(self, mv):
        r_mod = [0,-1,0,1]
        c_mod = [-1,0,1,0]

        move_tile = [self.blank_pos[0] + r_mod[mv.value], self.blank_pos[1] + c_mod[mv.value]]
        if(move_tile[0] < 0 or move_tile[0] >= 3 or move_tile[1] < 0 or move_tile[1] >= 3): # invald position
            raise Exception("Illegal move")
        
        self.matr[self.blank_pos[0]][self.blank_pos[1]], self.matr[move_tile[0]][move_tile[1]] = self.matr[move_tile[0]][move_tile[1]], self.matr[self.blank_pos[0]][self.blank_pos[1]]
        self.blank_pos = [move_tile[0], move_tile[1]]

    def __eq__(self, other):
        return self.matr == other.matr
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.matr))
    
    def self_legal_shuffle(self, iter):
        moves = [move.LEFT, move.UP, move.RIGHT, move.DOWN]
        for i in range(iter):
            index = random.randint(0, 3)
            try:
                self.__self_move(moves[index])
            except Exception as e:
                pass
    def __lt__(self, other):
        return False
    def __gt__(self, other):
        return False
