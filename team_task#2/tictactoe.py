from enum import Enum
from copy import deepcopy
import random

'''
보드판에 들어갈 'O','X','비어있음'을 Enum으로 정의 
'''
class Mark(Enum):
    X = 'X'
    O = 'O'
    EMPTY = '.'

class TicTaeToe:
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.cur_state = [
            [Mark.EMPTY,Mark.EMPTY,Mark.EMPTY],
            [Mark.EMPTY,Mark.EMPTY,Mark.EMPTY],
            [Mark.EMPTY,Mark.EMPTY,Mark.EMPTY]
        ]

    '''
    보드판 출력
    '''
    def draw(self):
        for i in range(3):
            for j in range(3):
                print(self.cur_state[i][j].value,end=" ")
            print("\n")
        print("----------------------------------")

    '''
    O 또는 X가 입력될 수 있는 보드의 위치들을 배열에 넣어 반환 
    '''
    def actions(self,state):
        ret = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == Mark.EMPTY:
                    ret.append([i,j])
        return ret

    '''
    게임판에 O 또는 X를 새롭게 입력하여,
    새로운 게임판을 반환
    '''
    def result(self,state,action,player):
        temp_state = deepcopy(state)
        a_x, a_y = action
        temp_state[a_x][a_y] = player
        return temp_state

    '''
    게임 종료 여부 확인.
    종료여부(boolean) , 판세평가값(10 or -10 or 0)을 반환
    '''
    def terminal(self,state):
        check_pos = [0,1,2]
        for pos in check_pos:
            if state[pos][pos] != Mark.EMPTY:
                if state[pos][0] == state[pos][1] == state[pos][2] or \
                state[0][pos] == state[1][pos] == state[2][pos]:
                    return True, 10 if state[pos][pos] == Mark.X else -10
            if pos == 1 and state[pos][pos] != Mark.EMPTY:
                if state[0][0] == state[1][1] == state[2][2] or \
                    state[0][2] == state[1][1] == state[2][0]:
                    return True, 10 if state[pos][pos] == Mark.X else -10
        
        is_tie = True
        for i in range(3):
            if is_tie == True:
                for j in range(3):
                    if state[i][j] == Mark.EMPTY:
                        is_tie = False
                        break            
        if is_tie == True:
            return True, 0
        return False, 0

    def max_value(self,state,depth):
        value = -999999999
        is_end, utility = self.terminal(state)
        if is_end:
            return (utility - depth, 0, 0)
        else:
            x = None
            y = None
            for a in self.actions(state):
                cur_v, _, _ = self.min_value(self.result(state,a,Mark.X),depth + 1)
                if value <= cur_v:
                    value = cur_v
                    x, y = a
            return (value, x, y)

    def min_value(self,state,depth):
        value = 999999999
        is_end, utility = self.terminal(state)
        if is_end:
            return (utility - depth, 0, 0)
        else:
            x = None
            y = None
            for a in self.actions(state):
                cur_v, _, _ = self.max_value(self.result(state,a,Mark.O),depth + 1)
                if value >= cur_v:
                    value = cur_v
                    x, y = a
            return (value, x, y)

    def start(self):
        print("---------Tic Tae Toe Start!----------")
        print("AI Turn(X)")
        self.cur_state = self.result(self.cur_state,[random.randrange(0,2),random.randrange(0,2)],Mark.X)
        self.draw()

        while True:
            print("Your Turn(O)")
            print("x (0~2) : ",end="")
            x = input()
            print("y (0~2) : ",end="")
            y = input()

            if x.isnumeric() and y.isnumeric():
                x, y = int(x), int(y)
            else:
                print("you must input number!\n")
                continue

            if 0 <= x <= 2 and 0 <= y <= 2 and self.cur_state[x][y] == Mark.EMPTY:
                self.cur_state = self.result(self.cur_state,[x,y],Mark.O)
                self.draw()

                min_is_end, min_utility = self.terminal(self.cur_state)
                if not min_is_end:
                    print("AI Turn(X)")
                    _, x, y = self.max_value(self.cur_state,0)
                    self.cur_state = self.result(self.cur_state,[x,y],Mark.X)
                    self.draw()

                    max_is_end, max_utility = self.terminal(self.cur_state)
                    if max_is_end:
                        return max_utility
                else:
                    return min_utility
            else:
                print("wrong position!\n")

    def end(self,utility):
        if utility == 10:
            print("AI(X) win!")
        elif utility == -10:
            print("You(O) win!")
        else:
            print("draw!")

if __name__ == '__main__':
    tic_tae_toe = TicTaeToe()
    game_result = tic_tae_toe.start()
    tic_tae_toe.end(game_result)