# self == astar
def manhattan_distance(self):
    sum = 0
    for i in range(8):
        bx, by = i // 3 , i % 3
        g_val = self.goal_pos[self.board[i]]
        gx, gy = g_val // 3 , g_val % 3
        sum += abs(bx - gx) + abs(by - gy)
    return sum