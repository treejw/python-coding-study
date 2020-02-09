import sys
input_func = sys.stdin.readline

if __name__ == '__main__':
    day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    M, D = map(int, input_func().split())
    days = sum(day_list[:M]) + D
    week_idx = days % 7
    print(week_list[week_idx])