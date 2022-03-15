import re

x = input()
check = re.fullmatch('(100+1+|01)+', x)
if check:
    print('SUBMARINE')
else:
    print('NOISE')