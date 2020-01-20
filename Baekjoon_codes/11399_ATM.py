N = int(input())

minuteList = list(map(int, input().strip().split()))
minuteList.sort()

timeRequired = [sum(minuteList[:i+1]) for i in range(N)]

print(sum(timeRequired))