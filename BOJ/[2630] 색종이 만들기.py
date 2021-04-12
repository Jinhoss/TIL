# import sys
# sys.stdin = open('input.txt')

def check(x, y, n):
    w, b = 0, 0
    # 배열을 돌며 배열 내 흰색, 파랑색의 개수를 체크
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] == 1:
                b += 1
            else:
                w += 1
            # 흰색, 파랑색이 섞여있으면 분할하여 검사
            if w and b:
                check(x, y, n//2)
                check(x + n//2, y, n//2)
                check(x, y + n//2, n//2)
                check(x + n//2, y + n//2, n//2)
                return
    # 단일 색인 경우 해당 색의 카운트 값을 기록한다.
    if w:
        cnt[0] += 1
    elif b:
        cnt[1] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# cnt[0]에는 흰색, cnt[1]에는 파랑색의 갯수를 체크
cnt = [0, 0]
check(0, 0, len(arr))
print(cnt[0])
print(cnt[1])
