import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    N = int(input_func())
    dp_arr = [0] + [1] * 9  # 0 1 1 1 1 1 1 1 1 1

    for digit in range(2, N + 1):  # 십의자리수부터
        dp_prev = dp_arr.copy()
        dp_arr[0] = dp_prev[1]
        dp_arr[9] = dp_prev[8]
        for i in range(1, 9):
            dp_arr[i] = dp_prev[i - 1] + dp_prev[i + 1]

    print(sum(dp_arr) % 1000000000)