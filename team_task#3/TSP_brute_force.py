import pandas as pd
from itertools import permutations

def solution(dist_table):
    print(len(dist_table),len(dist_table[0]))
    temp = [i for i in range(9)]
    min_val = 999999999
    min_subject = []
    subject_iter = permutations(temp) # len : 362880
    for subject in subject_iter:
        val = 0
        prev_node = subject[0]
        for i in range(1,9):
            node = subject[i]
            val += int(dist_table[prev_node][node])
            prev_node = node
        val += int(dist_table[subject[8]][subject[0]])
        if val < min_val:
            min_val = val
            min_subject = subject
    print("최단 경로 : " + str(min_subject))
    print("최단 거리 : " + str(min_val))
    # 최단 경로 : (0, 1, 2, 8, 7, 6, 5, 4, 3)
    # 최단 거리 : 1018

def main():
    df = pd.read_excel('distance.xlsx',header=1,usecols=range(1,10))
    dist_table = df.values.tolist()
    solution(dist_table)

if __name__ == "__main__":
    main()