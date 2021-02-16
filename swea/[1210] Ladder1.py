# import sys
# sys.stdin=open("Ladder_input.txt")

#도착지점인 2부터 시작해서 출발점까지 역으로 계산
#우선 도착지점 2인 컬럼을 탐색
def find_target(arr):
    for idx in range(len(arr)):
        if arr[99][idx]==2:
            return idx

#방향을 위쪽, 왼쪽, 오른쪽으로 나누어서 진행, 왼쪽으로 가다가 오른쪽으로 되돌아가는 걸 방지
#왼쪽이나 오른쪽으로 이동 중일땐 위쪽으로 갈 수 있는지를 먼저 확인
#위쪽으로 갈 때는 왼쪽이나 오른쪽으로 갈 수 있는지를 먼저 확인
#row가 0인 첫번째줄에 도착하면 컬럼 위치를 반환
def solution(arr,target):
    row=99
    column=target
    dir='U'
    while row>0:
        if dir=='U':
            if 0<=column-1<100 and arr[row][column-1]==1:
                column-=1
                dir='L'
            elif 0<=column+1<100 and arr[row][column+1]==1:
                column+=1
                dir='R'
            else:
                row-=1
        elif dir=='L':
            if arr[row-1][column]==1:
                row-=1
                dir='U'

            else:
                column-=1
        else:
            if arr[row-1][column]==1:
                row-=1
                dir='U'

            else:
                column+=1
    return column
#인풋값 입력후 위에 작성한 함수에 차례대로 대입
for _ in range(10):
    tc=int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    t_idx=find_target(arr)
    result=solution(arr,t_idx)
    print('#{} {}'.format(tc,result))