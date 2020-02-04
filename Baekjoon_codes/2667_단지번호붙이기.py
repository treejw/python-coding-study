import sys
input_func = sys.stdin.readline

def BFS(N, Map, passed, start):
    queue = [start]
    num_house = 1
    while queue:
        (cur_x, cur_y) = queue.pop(0)
        passed.add( (cur_x, cur_y) )
        for (x, y) in [(cur_x + 1, cur_y), (cur_x, cur_y + 1), (cur_x - 1, cur_y), (cur_x, cur_y - 1)]:
            if (x < 0 or x >= N) or (y < 0 or y >= N) or (x, y) in passed:
                continue
            passed.add((x, y))
            if Map[x][y] == '1':
                queue.append( (x, y) )
                num_house += 1
    return num_house, passed

def search_complex(N, Map):
    each_n_house = []
    passed = set()
    for i in range(N):
        for j in range(N):
            if (i, j) in passed:
                continue
            elif Map[i][j] == '1':
                start = (i, j)
                num_house, passed = BFS(N, Map, passed, start)
                each_n_house.append(num_house)
    return each_n_house

if __name__ == '__main__':
    N = int(input_func())
    Map = list()
    for _ in range(N):
        Map.append(list(input_func().strip()))
    each_n_house = search_complex(N, Map)
    print(len(each_n_house))
    print(*sorted(each_n_house), sep='\n')
