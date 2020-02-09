import sys
input_func = sys.stdin.readline

def stairs_DP(stairs):
    DP_arr = []
    for i, cur_stair in enumerate(stairs):
        if i in [0, 1, 2]:
            DP_arr.append( sum(stairs[:i+1]) )
        else:
            # (전전전계단 누적점수 + 전계단 점수) vs (전전계단 누적점수)
            prev_max = max( DP_arr[i-3] + stairs[i-1], DP_arr[i-2] )
            DP_arr.append( prev_max + cur_stair )
    return DP_arr[-1]

if __name__ == '__main__':
    N = int(input_func())
    stairs = [0] + [int(input_func()) for _ in range(N)]
    max_score = stairs_DP(stairs)
    print(max_score)