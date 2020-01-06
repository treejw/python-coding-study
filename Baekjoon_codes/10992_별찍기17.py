if __name__ == '__main__':
    N = int(input())

    for i in range(1, N+1):
        string = ' ' * (N-i)

        if (i != 1) and (i != N):
            sep = ' ' * ((i - 1) * 2 - 1)
            temp = sep.join(['*', '*'])
            string += temp
        else:
            string += '*' * (i*2 - 1)

        print(string)