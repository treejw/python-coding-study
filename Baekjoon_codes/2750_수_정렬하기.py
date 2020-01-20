import sys
sys.setrecursionlimit(10**6)

def Bubble_Sort(N, arr):
    for i in range(N-1):
        for j in range(i, N):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i], arr[j] = arr[j], tmp
    return arr

def Quick_Sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[0]
    left =  [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return Quick_Sort(left) + [pivot] + Quick_Sort(right)


if __name__ == '__main__':
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    # arr = Bubble_Sort(N, arr)
    arr = Quick_Sort(arr)
    print(*arr, sep='\n', end='')