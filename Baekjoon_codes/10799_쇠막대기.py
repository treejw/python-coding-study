import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    string = input_func().strip()
    count = 0
    prev = ''
    stack = []
    for x in string:
        if x == '(':  stack.append(x)
        else:
            if prev == '(':   # 레이저
                stack.pop()
                count += len(stack)
            elif prev == ')': # 막대기 끝
                stack.pop()
                count += 1
        prev = x
    print(count)