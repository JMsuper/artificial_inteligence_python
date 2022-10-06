answer = 0

def recursive(k,need_list,cur_k,cur_list):
    global answer
    new_list = cur_list[:]
    if k == cur_k:
        print(cur_list)
        answer += 1
    elif cur_k > k:
        return
    else:
        for item in need_list:
            if cur_k == 0 and item == 0:
                continue
            recursive(k,need_list,cur_k+item,new_list+[item])

def solution(k):
    global answer
    need_list = [6,2,5,5,4,5,6,3,7,6]
    recursive(k,need_list,0,[])
    return answer

def main():
    k = 11
    print(solution(k))

if __name__ == "__main__":
    main()