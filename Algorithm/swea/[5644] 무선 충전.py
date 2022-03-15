import sys
sys.stdin = open('input.txt')

def charge(ax, ay, bx, by):
    global result
    a_charge = []
    b_charge = []
    for i in range(A):
        x, y, C, P = AP[i]
        if abs(ax - x) + abs(ay - y) <= C:
            a_charge.append((i, P))
        if abs(bx - x) + abs(by - y) <= C:
            b_charge.append((i, P))

    a_charge.sort(key=lambda x: x[1], reverse=True)
    b_charge.sort(key=lambda x: x[1], reverse=True)

    used = 0
    temp1 = 0
    for idx, P in a_charge:
        used = idx
        temp1 += P
        break
    for idx, P in b_charge:
        if idx != used:
            temp1 += P
            break
    temp2 = 0
    for idx, P in b_charge:
        used = idx
        temp2 += P
        break
    for idx, P in a_charge:
        if idx != used:
            temp2 += P
            break

    result += max(temp1, temp2)


delta = {0:(0, 0), 1:(0, -1), 2:(1, 0), 3:(0, 1), 4:(-1, 0)}
T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    route = [list(map(int, input().split())) for _ in range(2)]
    AP = [list(map(int, input().split())) for _ in range(A)]

    Ax, Ay = 1, 1
    Bx, By = 10, 10
    result = 0
    charge(Ax, Ay, Bx, By)
    for i in range(M):
        Ad, Bd = route[0][i], route[1][i]
        a_dx, a_dy = delta[Ad]
        b_dx, b_dy = delta[Bd]
        Ax, Ay = Ax + a_dx, Ay + a_dy
        Bx, By = Bx + b_dx, By + b_dy
        charge(Ax, Ay, Bx, By)

    print('#{} {}'.format(tc, result))