T = int(input())


def solution(depth, sub_sum):
    global min_value
    for i in range(N):
        if not check[i]:
            check[i] = True
            sub_sum += matrix[depth][i]
            if sub_sum < min_value:
                if depth == N - 1:
                    min_value = sub_sum
                else:
                    solution(depth + 1, sub_sum)
            sub_sum -= matrix[depth][i]
            check[i] = False


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [False] * N
    min_value = float('inf')
    solution(0, 0)
    print("#{} {}".format(tc, min_value))