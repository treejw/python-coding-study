import sys
input_func = sys.stdin.readline

def count_paper(white_count, blue_count, N, paper_map):
    if len(paper_map) == 0:
        return white_count, blue_count
    if '0' not in sum(paper_map, []):
        return white_count, blue_count+1
    elif '1' not in sum(paper_map, []):
        return white_count+1, blue_count
    white_count, blue_count = count_paper(white_count, blue_count, N//2, [x[:N//2] for x in paper_map[:N//2]])
    white_count, blue_count = count_paper(white_count, blue_count, N//2, [x[N//2:] for x in paper_map[:N//2]])
    white_count, blue_count = count_paper(white_count, blue_count, N//2, [x[:N//2] for x in paper_map[N//2:]])
    white_count, blue_count = count_paper(white_count, blue_count, N//2, [x[N//2:] for x in paper_map[N//2:]])
    return white_count, blue_count

if __name__ == '__main__':
    N = int(input_func())
    paper_map = [list(input_func().split()) for _ in range(N)]
    white_count, blue_count = count_paper(white_count=0, blue_count=0, N=N, paper_map=paper_map)
    print(white_count, blue_count, sep='\n')