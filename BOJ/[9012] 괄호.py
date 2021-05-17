N = int(input())
for _ in range(N):
    q = []
    word = list(input())
    for w in word:
        if w == '(':
            q.append(w)
        else:
            if q:
                q.pop()
            else:
                print('NO')
                break
    else:
        if q:
            print('NO')
        else:
            print('YES')
