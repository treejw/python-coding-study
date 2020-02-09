import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    input_split = input_func().strip().split('-')
    result = 0
    for i, x in enumerate(input_split):
        temp = sum(map(int, x.split('+'))) if ('+' in x)  else int(x)
        result = result - temp if (i != 0) else temp
    print(result)