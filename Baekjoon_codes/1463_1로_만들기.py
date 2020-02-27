import sys

input_func = sys.stdin.readline

if __name__ == '__main__':
    N = int(input_func())
    DP_arr = [0] * (N + 1)

    for i in range(1, N):
        if (i + 1 <= N) and (DP_arr[i + 1] == 0 or DP_arr[i + 1] > DP_arr[i] + 1):
            DP_arr[i + 1] = DP_arr[i] + 1
        if (i * 2 <= N) and (DP_arr[i * 2] == 0 or DP_arr[i * 2] > DP_arr[i] + 1):
            DP_arr[i * 2] = DP_arr[i] + 1
        if (i * 3 <= N) and (DP_arr[i * 3] == 0 or DP_arr[i * 3] > DP_arr[i] + 1):
            DP_arr[i * 3] = DP_arr[i] + 1

    #                        1  2  3  4  5  6  7  8  9  10
    # N = 10 -> DP_arr = [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
    print(DP_arr[N])
