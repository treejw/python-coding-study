from collections import deque
import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    N = int(input_func())
    cards = deque(range(1, N+1))
    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())
    print(cards[0])