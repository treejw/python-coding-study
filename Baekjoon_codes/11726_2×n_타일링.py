import sys

def DP_tiling(n):
    global DP_save
    if DP_save[n]:
        return DP_save[n]
    else:
        if n == 1:
            DP_save[n] = 1
        elif n == 2:
            DP_save[n] = 2
        else:
            DP_save[n] = DP_tiling(n-2) + DP_tiling(n-1)
        return DP_save[n]
    
if __name__ == '__main__':
    # 1 -> 1    2 -> 2    3 -> 3    4 -> 5    5 -> 8    6 -> 13
    n = int(sys.stdin.readline())
    DP_save = [0]*(n+1)
    print(DP_tiling(n) % 10007)
