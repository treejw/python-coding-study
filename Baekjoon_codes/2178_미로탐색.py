def BFS(N, M, arr):
    start, goal = (0, 0), (N - 1, M - 1)
    cur_step = 1
    queue = [(cur_step, start)]  # (1, (0, 0))
    passed = set()

    arrival = False
    while not arrival:
        (step, (cur_x, cur_y)) = queue.pop(0)
        passed.add((cur_x, cur_y))
        for (x, y) in [(cur_x + 1, cur_y), (cur_x, cur_y + 1), (cur_x - 1, cur_y), (cur_x, cur_y - 1)]:
            if (x < 0 or x >= N) or (y < 0 or y >= M) or (x, y) in passed: continue
            if arr[x][y] == 1:
                new_step = step + 1
                if cur_step <= new_step: cur_step = new_step
                if (x, y) == goal:
                    return cur_step
                queue.append((new_step, (x, y)))
                passed.add((x, y))

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    arr = list()
    for _ in range(N): arr.append(list(map(int, list(input().strip()))))
    print(BFS(N, M, arr))