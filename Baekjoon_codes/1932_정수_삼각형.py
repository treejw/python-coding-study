import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    N = int(input_func())
    arr = [[0] + list(map(int, input_func().split())) + [0] for _ in range(N)]
    for i, line in enumerate(arr):
        if i == 0: continue
        temp_line = []
        for j, x in enumerate(line):
            if j == 0 or j == len(line)-1: continue     # zero padding
            temp_line.append(x + max(arr[i-1][j-1], arr[i-1][j]))
        arr[i][1:-1] = temp_line
    print(max(arr[-1]))