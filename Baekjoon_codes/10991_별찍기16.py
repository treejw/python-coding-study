if __name__ == '__main__':
    N = int(input())

    for i in range(1, N+1):
        string = ' ' * (N-i)
        temp = ['*'] * i
        temp = ' '.join(temp)
        string += temp
        print(string)