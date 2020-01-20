import sys

def countingSort():
    count_arr = [0] * 10001  # 1 <= num(index) <= 10000
    for _ in range(int(sys.stdin.readline())):
        count_arr[int(sys.stdin.readline())] += 1
    for num, count in enumerate(count_arr):
        for _ in range(count): print(num)

countingSort()