import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    N = int(input_func())
    meeting_list = [tuple(map(int, input_func().split())) for _ in range(N)]
    meeting_list.sort(key=lambda x: x[0])
    meeting_list.sort(key=lambda x: x[1])
    num_meeting = 0
    prev_end_time = 0
    for start, end in meeting_list:
        if start >= prev_end_time:
            num_meeting += 1
            prev_end_time = end

    print(num_meeting)
