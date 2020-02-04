import sys
input_func = sys.stdin.readline

def DP_RGB(n, cost_RGB):
    DP_arr = []
    DP_arr.append(cost_RGB[0])
    for i in range(1, n):
        pre_R, pre_G, pre_B = DP_arr[i-1][0], DP_arr[i-1][1], DP_arr[i-1][2]
        cur_R = cost_RGB[i][0] + min(pre_G, pre_B)
        cur_G = cost_RGB[i][1] + min(pre_R, pre_B)
        cur_B = cost_RGB[i][2] + min(pre_R, pre_G)
        DP_arr.append([cur_R, cur_G, cur_B])

    return min(DP_arr[-1])

if __name__ == '__main__':
    N = int(input_func())
    cost_RGB = [list(map(int, input_func().split())) for _ in range(N)]
    print(DP_RGB(N, cost_RGB))
