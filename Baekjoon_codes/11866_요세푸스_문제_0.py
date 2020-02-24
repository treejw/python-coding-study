import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input_func().split())
    arr = list(map(str, range(1, N+1)))
    result = []
    while len(arr) != 0:
        for i in range(K-1):        # 맨 앞 숫자를 맨 뒤로 이동
            arr.append(arr.pop(0))
        result.append(arr.pop(0))   # 맨 앞 숫자 제거 & 출력
    print('<{}>'.format(', '.join(result)))