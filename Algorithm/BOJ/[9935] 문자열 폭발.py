word = input()
bomb = input()
result = []
for w in word:
    result.append(w)
    if len(result) >= len(bomb):
        for idx in range(-1, -len(bomb) -1 , -1):
            if result[idx] != bomb[idx]:
                break
        else:
            for _ in range(len(bomb)):
                result.pop()
if not result:
    print('FRULA')
else:
    print(''.join(result))
