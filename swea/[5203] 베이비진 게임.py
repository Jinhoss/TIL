def baby(lst):
    i = 0
    while lst:
        if i % 2 == 0:
            player1[lst.pop(0)] += 1
            i += 1
            if 3 in player1:
                return 1
            for k in range(10):
                if player1[k % 10] and player1[(k + 1) % 10] and player1[(k + 2) % 10]:
                    return 1
        elif i % 2 == 1:
            player2[lst.pop(0)] += 1
            i += 1
            if 3 in player2:
                return 2
            for l in range(10):
                if player2[l % 10] and player2[(l + 1) % 10] and player2[(l + 2) % 10]:
                    return 2
    return 0


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    print('#{} {}'.format(tc, baby(lst)))
