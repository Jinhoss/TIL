import re
n = int(input())

for _ in range(n):
    if re.fullmatch('(100+1+|01)+', input()):
        print('YES')
    else:
        print('NO')