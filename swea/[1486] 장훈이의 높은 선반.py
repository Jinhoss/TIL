# import sys
# sys.stdin = open('input.txt')

T = int(input())

def top(idx, height):
    global min_height
    # B와 크거나 같고 최소값보다 작은 경우에만 갱신
    if B <= height < min_height:
        min_height = height
    if idx == N:
        return
    # 해당 인덱스의 키를 포함시키지 않는 경우
    top(idx+1, height)
    # 해당 인덱스의 키를 포함시키는 경우
    top(idx+1, height + height_lst[idx])

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height_lst = list(map(int, input().split()))
    # N의 최대값 20, B의 최대값이 10000이므로 200000으로 초기화
    min_height = 200000
    top(0, 0)
    print('#{} {}'.format(tc, min_height - B))
