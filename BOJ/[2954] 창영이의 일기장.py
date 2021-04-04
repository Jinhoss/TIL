import re

x = input()
for s in ['a', 'e', 'i', 'o', 'u']:
    x = re.sub(f'{s}p{s}', s, x)
print(x)