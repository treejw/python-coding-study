from collections import deque
import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    N_testcase = int(input_func())
    res = []
    for _ in range(N_testcase):
        num_papers, q_paper_idx = map(int, input_func().split())
        importance = deque(map(int, input_func().split()))  # importance = deque([1, 1, 9, 1, 1, 1])
        papers = deque(range(num_papers))                   # papers     = deque([0, 1, 2, 3, 4, 5])

        count = 1
        while len(papers) != 0:
            if importance[0] >= max(importance):
                if papers[0] == q_paper_idx:
                    res.append(count)
                    break
                importance.popleft()
                papers.popleft()
                count += 1
            else:
                importance.append(importance.popleft())
                papers.append(papers.popleft())

    print(*res, sep='\n')