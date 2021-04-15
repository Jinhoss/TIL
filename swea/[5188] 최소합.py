# import sys
# sys.stdin = open('input.txt')

T = int(input())

def subSum(x, y, cnt, value):
    global result
   # 현재 값이 저장되어 있는 최소값보다 크다면 더 이상 확인할 필요가 없음
    if value > result:
        return
    # 정해진 횟수만큼 이동을 한 경우 최소값보다 작은지 체크
    if cnt == num:
        if value < result:
            result = value
            return
    # 오른쪽 또는 아래쪽으로 이동하며 체크한다.
    for dx, dy in [(0, 1), (1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            subSum(nx, ny, cnt + 1, value + arr[nx][ny])


for tc in range(1, T + 1):
    # 숫자, 배열 입력
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 총 진행횟수
    num = 2 * (N - 1)
    # 최대값 초기화
    result = 2 * 10 * N
    subSum(0, 0, 0, arr[0][0])
    print('#{} {}'.format(tc, result))