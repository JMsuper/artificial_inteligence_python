def heuristic(not_used_color_list,cur_node,adj_dict,region_color_dict):
    color_cnt = [0,0,0,0]
    visited = set()
    adj_list = adj_dict[cur_node]
    for i in adj_list:
        if not i in region_color_dict:
            for j in adj_dict[i]:
                if j in region_color_dict and not j in visited:
                    color_cnt[region_color_dict[j]] += 1
                    visited.add(j)
    
    cur_idx = -1
    cur_cnt = -1
    for color_idx in not_used_color_list:
        if color_cnt[color_idx] > cur_cnt:
            cur_idx = color_idx
            cur_cnt = color_cnt[color_idx]
    return cur_idx

def find_not_used_color(region_color_dict,adj_list):
    color_set = set()
    for adj_idx in adj_list:
        if adj_idx in region_color_dict:
            color_set.add(region_color_dict[adj_idx])
    return list(set([0,1,2,3]) - color_set)


def solution(adj_dict,node_cnt):
    region_color_dict = {}
    for i in range(node_cnt):
        adj_list = adj_dict[i]
        not_used_color_list = find_not_used_color(region_color_dict,adj_list)
        if not not_used_color_list:
            print(i)
            exit()
        color_idx = heuristic(not_used_color_list,i,adj_dict,region_color_dict)
        region_color_dict[i] = color_idx
    ret_list = [-1 for _ in range(node_cnt)]
    for key, value in region_color_dict.items():
        ret_list[key] = value
    return ret_list

def main():
    node_name_list = [
        "seoul","incheon","gyeonggi","gangwon","chungnam","chungbuk","sejong","daejeon",#7
        "gyeongbuk","jeonbuk","daegu","ulsan","jeonnam","busan","gwangju","gyeongnam"#15
    ]
    color_list = ["빨","주","노","초"]
    node_cnt = 16
    adj_dict = {}
    adj_dict[0] = [1,2]
    adj_dict[1] = [0,2]
    adj_dict[2] = [0,1,3,4,5]
    adj_dict[3] = [2,5,8]
    adj_dict[4] = [2,5,6,7,9]
    adj_dict[5] = [2,3,4,6,7,9,8]
    adj_dict[6] = [4,5,7]
    adj_dict[7] = [4,5,6,9]
    adj_dict[8] = [3,5,9,10,11,15]
    adj_dict[9] = [4,5,7,8,15,12]
    adj_dict[10] = [8,15]
    adj_dict[11] = [8,15,13]
    adj_dict[12] = [9,14,15]
    adj_dict[13] = [11,15]
    adj_dict[14] = [12]
    adj_dict[15] = [8,9,10,11,12,13]
    ret_list = solution(adj_dict,node_cnt)
    for i in range(node_cnt):
        print(node_name_list[i] + " : " + color_list[ret_list[i]])

    return
if __name__ == "__main__":
    main()