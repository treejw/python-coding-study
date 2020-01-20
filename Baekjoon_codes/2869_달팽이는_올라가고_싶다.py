import math
A, B, V = map(int, input().strip().split())
# V <= A*day - B*(day-1) --> V <= (A-B)*day + B  --> (V-B) / (A-B) <= day
print(math.ceil((V-B)/(A-B)))