import sys
input_func = sys.stdin.readline

def check_paper(paper_map):
    paper_flag = True
    for line in paper_map:
        for x in line:
            if paper_map[0][0] != x:
                paper_flag = False
                break
    return paper_flag

def count_paper(count_dict, N, paper_map):
    if len(paper_map) == 0:
        return count_dict
    # check value
    paper_flag = check_paper(paper_map)
    if paper_flag:
        if  paper_map[0][0] == '-1':  count_dict['-1'] += 1
        elif paper_map[0][0] == '0':  count_dict[ '0'] += 1
        elif paper_map[0][0] == '1':  count_dict[ '1'] += 1
        return count_dict
    # divide paper
    N = N//3
    for i in range(3):
        for j in range(3):
            count_dict = count_paper(count_dict, N, [x[N*i:N*(i+1)] for x in paper_map[N*j:N*(j+1)]])
    return count_dict

if __name__ == '__main__':
    N = int(input_func())
    paper_map = [list(input_func().split()) for _ in range(N)]
    count_dict = {'-1': 0, '0': 0, '1': 0}   # -1, 0, 1 의 각 종이 개수
    count_dict = count_paper(count_dict, N, paper_map)
    print(count_dict['-1'], count_dict['0'], count_dict['1'], sep='\n')