import sys
input_func = sys.stdin.readline

def max_num(score_arr):
    score_arr.sort()    # 서류점수 기준으로 순위가 높은 순으로 정렬
    count = 1
    standard_interview = score_arr[0][1]    # 면접순위 마지노선
    for document, interview in score_arr[1:]:
        if interview < standard_interview:
            count += 1
            standard_interview = interview
    return count

if __name__ == '__main__':
    result = []
    T = int(input_func())
    for _ in range(T):
        N = int(input_func())
        score_arr = [tuple(map(int, input_func().split())) for _ in range(N)]
        result.append(max_num(score_arr))
    print(*result, sep='\n')