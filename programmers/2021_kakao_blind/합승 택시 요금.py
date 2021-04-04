def solution(n, s, a, b, fares):
    arr = [[float('inf')] * (n+1) for _ in range(n+1)]
    for fare in fares:
        v, e, cost = fare
        arr[v][e] = cost
        arr[e][v] = cost
    for path in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n+1):
                if start == end:
                    arr[start][end] = 0
                else:
                    if arr[start][end] > arr[start][path] + arr[path][end]:
                        arr[start][end] = arr[start][path] + arr[path][end]
    min_v = arr[s][a] + arr[s][b]
    for path in range(1, n + 1):
        if min_v > arr[s][path] + arr[path][a] + arr[path][b]:
            min_v = arr[s][path] + arr[path][a] + arr[path][b]
    return min_v

if __name__ == '__main__':
    n, s, a, b = 6, 4, 6, 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n, s, a, b, fares))