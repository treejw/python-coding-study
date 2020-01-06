from itertools import combinations

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    cards = list(map(int, input().strip().split()))

    comb_3cards = list(combinations(cards, 3))

    sum_3cards = [sum(c) for c in comb_3cards if sum(c) <= M]

    print(max(sum_3cards))