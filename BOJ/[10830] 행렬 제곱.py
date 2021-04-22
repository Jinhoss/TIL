import sys

N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def matric_mul(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A

    elif B % 2 == 1:
        tmp = [[0 for _ in range(N)] for _ in range(N)]
        C = matric_mul(A, B - 1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += C[i][k] * A[k][j]
                tmp[i][j] %= 1000

        return tmp

    else:
        tmp = [[0 for _ in range(N)] for _ in range(N)]
        C = matric_mul(A, B // 2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += C[i][k] * C[k][j]
                tmp[i][j] %= 1000
        return tmp


result = matric_mul(A, B)
for li in result:
    for p in li:
        print(p, end=' ')
    print()