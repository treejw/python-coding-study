import sys
input_func = sys.stdin.readline

def Quad_Tree(N, Map):
    if len(Map) == 0:
        return
    if '0' not in sum(Map, []):
        return '1'
    elif '1' not in sum(Map, []):
        return '0'
    string = '({}{}{}{})'.format(
        Quad_Tree(N//2, [x[:N//2] for x in Map[:N//2]]),
        Quad_Tree(N//2, [x[N//2:] for x in Map[:N//2]]),
        Quad_Tree(N//2, [x[:N//2] for x in Map[N//2:]]),
        Quad_Tree(N//2, [x[N//2:] for x in Map[N//2:]])
    )
    return string

if __name__ == '__main__':
    N = int(input_func())
    Map = [list(input_func().strip()) for _ in range(N)]
    string = Quad_Tree(N=N, Map=Map)
    print(string)