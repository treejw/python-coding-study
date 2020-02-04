import sys
input_func = sys.stdin.readline

def BFS(graph_dict, start, parent_dict):
    passed = set()
    queue = [start]
    while queue:
        cur_node = queue.pop(0)
        passed.add(cur_node)
        for node in graph_dict[cur_node]:
            if node not in passed:
                queue.append(node)
                parent_dict[node] = cur_node
    return parent_dict

if __name__ == '__main__':
    N = int(input_func())

    graph_dict, parent_dict = dict(), dict()
    for node in range(1, N+1):
        graph_dict[node] = list()
        parent_dict[node] = 0

    for _ in range(N - 1):
        x, y = map(int, input_func().split())
        graph_dict[x].append(y)
        graph_dict[y].append(x)

    BFS(graph_dict, 1, parent_dict)

    for i in range(2, N+1):
        print(parent_dict[i])
