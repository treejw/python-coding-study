if __name__ == '__main__':
    N = int(input())

    max_num_5kg = N // 5

    for i in range(max_num_5kg, -1, -1):
        if (N - 5*i) % 3 != 0:
            pass
        else:
            print(i + (N - 5*i) // 3)
            break
    else:
        print(-1)