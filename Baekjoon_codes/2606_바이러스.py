# https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html
# https://gmlwjd9405.github.io/2018/08/15/algorithm-bfs.html

import sys
input_func = sys.stdin.readline

def DFS(graph_dict, cur_node, passed):
    if cur_node not in passed:
        passed.append(cur_node)
        nodes = sorted(graph_dict[cur_node] - set(passed))
        for node in nodes:
            passed = DFS(graph_dict, node, passed)
    return passed

def BFS(graph_dict, start):
    passed = list()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in passed:
            passed.append(node)
            queue.extend(sorted(graph_dict[node] - set(passed)))
    return passed

if __name__ == '__main__':
    N, M, V = map(int, input_func().split())

    graph_dict = {node: set() for node in range(1, N+1)}
    for _ in range(M):
        x, y = map(int, input_func().split())
        graph_dict[x].add(y)
        graph_dict[y].add(x)

    result_dfs = DFS(graph_dict, V, [])
    print(*result_dfs)
    result_bfs = BFS(graph_dict, V)
    print(*result_bfs, end='')
