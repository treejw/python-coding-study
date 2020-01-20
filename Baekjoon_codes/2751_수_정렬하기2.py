# PyPy3

N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]
arr.sort()
print(*arr, sep='\n', end='')