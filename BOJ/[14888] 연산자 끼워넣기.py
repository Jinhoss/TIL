# 백트래킹으로 연산을 수행하며 최대값, 최소값을 저장하였다.
def cal(idx, result):
    global min_v, max_v
    if idx == N - 1:
        if result < min_v:
            min_v = result
        if result > max_v:
            max_v = result
        return
    x, y = result, num_lst[idx + 1]
    # 연산자의 남아있는 개수를 확인하며 연산을 수행한다.
    if oper_lst[0]:
        oper_lst[0] -= 1
        cal(idx + 1, x + y)
        oper_lst[0] += 1
    if oper_lst[1]:
        oper_lst[1] -= 1
        cal(idx + 1, x- y)
        oper_lst[1] += 1
    if oper_lst[2]:
        oper_lst[2] -=1
        cal(idx + 1, x * y)
        oper_lst[2] += 1
    if oper_lst[3]:
        oper_lst[3] -= 1
        cal(idx + 1, int(x / y))
        oper_lst[3] += 1


max_v = -1000000000
min_v = 1000000000
N = int(input())
num_lst = list(map(int, input().split()))
oper_lst = list(map(int, input().split()))
cal(0, num_lst[0])
print(max_v)
print(min_v)
