# import sys
# sys.stdin=open("sort_input.txt")
#선택정렬 구현
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    print('#{}'.format(tc), *lst)
