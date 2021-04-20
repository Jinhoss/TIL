def quick_sort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quick_sort(A, l, s - 1)
        quick_sort(A, s + 1, r)


def partition(A, l, r):
    p = A[l]
    i = l + 1
    j = r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = list(map(int, input().split()))
    quick_sort(matrix, 0, n - 1)
    print("#{} {}".format(tc, matrix[n // 2]))

