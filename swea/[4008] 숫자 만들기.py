# import sys
# sys.stdin = open('input.txt')

# 연산 함수, idx:인덱스 , opi:i번째 연산자의 남은 횟수, result: 현재 연산값
def cal(idx, op1, op2, op3, op4, result):
    global min_v, max_v
    # idx == N, 즉 연산자를 모두 사용하고나서 최대값, 최소값 비교
    if idx == N:
        if result > max_v:
            max_v = result
        if result < min_v:
            min_v = result
        return
    # 각 연산자가 남아있다면 다음 연산을 진행
    if op1:
        cal(idx + 1, op1 - 1, op2, op3, op4, result + num_lst[idx])
    if op2:
        cal(idx + 1, op1, op2 - 1, op3, op4, result - num_lst[idx])
    if op3:
        cal(idx + 1, op1, op2, op3 - 1, op4, result * num_lst[idx])
    if op4:
        cal(idx + 1, op1, op2, op3, op4 - 1, int(result/num_lst[idx]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    num_lst = list(map(int, input().split()))
    # 최대값, 최소값 초기화
    max_v = float('-inf')
    min_v = float('inf')
    cal(1, op1, op2, op3, op4, num_lst[0])
    print('#{} {}'.format(tc, max_v - min_v))

