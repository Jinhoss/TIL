# import sys
# sys.stdin = open('input.txt')

N = int(input())
arr = [list(input()) for _ in range(N)]
# 가로, 세로 누울 수 있는 자리 초기화
row, col = 0, 0
# 가로로 누울 수 있는 곳 검사
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j] == '.' and j < N-1:
            cnt+=1
        elif arr[i][j] == '.' and j == N-1:
            cnt+=1
            if cnt>=2:
                row+=1
        # X가 나오면 여태 나온 .의 개수를 확인
        elif arr[i][j] == 'X':
            if cnt>=2:
                row+=1
            cnt = 0
# 세로로 누울 수 있는 자리 검사
for j in range(N):
    cnt = 0
    for i in range(N):
        if arr[i][j] == '.' and i < N-1:
            cnt+=1
        elif arr[i][j] == '.' and i == N-1:
            cnt+=1
            if cnt>=2:
                col+=1
        elif arr[i][j] == 'X':
            if cnt>=2:
                col+=1
            cnt = 0
print(row, col)
