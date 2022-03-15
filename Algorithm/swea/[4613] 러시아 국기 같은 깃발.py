# import sys
# sys.stdin = open('input.txt')

T = int(input())
# 모든 경우의 수에 대해 완전탐색
# 각 색깔에 해당하는 행의 개수가 몇 개인지 입력
def color_sum(w,b,r):
    idx = 0
    cnt = 0
    #각 개수만큼 색을 변환하며 바꾸는데 필요한 색의 개수를 저장
    while idx < w:
        cnt += len([x for x in arr[idx] if x != 'W'])
        idx+=1
    while idx < w+b:
        cnt += len([x for x in arr[idx] if x != 'B'])
        idx += 1
    while idx < n:
        cnt += len([x for x in arr[idx] if x != 'R'])
        idx += 1
    return cnt

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    result = 0
    min_v = float('inf')
    # 각 색깔의 개수에 대한 모든 경우의 수를 탐색
    for i in range(1, n-1):
        for j in range(1, n-i):
            result = color_sum(i, j, n-j-i)
            if result < min_v:
                min_v = result
    print('#{} {}'.format(tc, min_v))

