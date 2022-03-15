a = input()
b = input()

while len(a)<len(b):
    if b[-1] == 'A':
        b =b[:-1]
    else:
        b = b[:-1]
        b = b[::-1]
if a == b:
    print(1)
else:
    print(0)