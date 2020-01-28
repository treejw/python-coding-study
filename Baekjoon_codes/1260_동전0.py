N, K = map(int, input().split())
coin_list = [int(input()) for _ in range(N)]

count = 0
for coin in coin_list[::-1]:
    count_temp = K // coin
    count += count_temp
    K -= coin * count_temp
print(count)
