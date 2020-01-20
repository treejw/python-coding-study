def get_height_width(n):
    height = 2 ** n - 1
    width = height * 2 - 1
    return height, width

def triangle(init_y, init_x, n, h, w, arr):
    for i in range(h):
        num_front_space = (h - 1) - i if n % 2 != 0 else i

        y, x = init_y + i, init_x + num_front_space
        arr[y][init_x:x] = [' '] * num_front_space

        if (n % 2 != 0 and i == 0) or (n % 2 == 0 and i == h - 1):
            arr[y][x] = '*'
        elif (n % 2 != 0 and i == h - 1) or (n % 2 == 0 and i == 0):
            arr[y][x:x + w] = ['*'] * w
        else:
            num_sep = i * 2 - 1 if n % 2 != 0 else ((h - 1) - i) * 2 - 1
            arr[y][x:x + num_sep + 2] = ['*'] + [' '] * num_sep + ['*']
    return arr


if __name__ == '__main__':
    N = int(input().strip())
    if N == 1:  print('*')
    else:
        total_height, total_width = get_height_width(N)
        arr = [list([''] * total_width) for i in range(total_height)]  # arr[y][x]

        init_y, init_x = 0, 0
        for i in range(N, 0, -1):
            h_i, w_i = get_height_width(i)
            arr = triangle(init_y, init_x, i, h_i, w_i, arr)
            if i % 2 != 0:
                init_y, init_x = init_y + h_i // 2, init_x + 2 ** (i - 1)
            else:
                init_y, init_x = init_y + 1, init_x + 2 ** (i - 1)

        for i in range(total_height):  print(*arr[i], sep='')