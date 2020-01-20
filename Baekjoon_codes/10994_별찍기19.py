N = int(input().strip())

lines = ['*']
for step in range(2, N+1):
    for i, line in enumerate(lines): lines[i] = '* ' + line + ' *'
    tmp = '*' + ' '*(4*(step-1)-1) + '*'
    lines.insert(0, tmp); lines.insert(len(lines), tmp)
    tmp = '*'*len(tmp)
    lines.insert(0, tmp); lines.insert(len(lines), tmp)

for line in lines: print(*line, sep='')