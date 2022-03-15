from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


# 톱니바퀴 회전
def rotation(lst, direction):
    # 시계 방향
    if direction == 1:
        lst = lst[-1] + lst[:-1]
    # 반시계 방향
    else:
        lst = lst[1:] + lst[0]
    return lst


# 현재 기어 오른쪽을 검사한다.
def check_right(number, direction):
    if number == 4:
        return
    if gear[number - 1][2] != gear[number][6]:
        q.append((number + 1, direction * (-1)))
        # 재귀적으로 검사
        check_right(number + 1, direction * (-1))
    else:
        return


# 현재 기어 왼쪽을 검사한다.
def check_left(number, direction):
    if number == 1:
        return
    if gear[number - 1][6] != gear[number - 2][2]:
        q.append((number - 1, direction * (-1)))
        # 재귀적으로 검사
        check_left(number - 1, direction * (-1))
    else:
        return


# 입력값에 \n이 포함되어 있음 rstrip을 안하면 틀리게 된다.
gear = [input().rstrip() for _ in range(4)]
K = int(input())
q = deque()
for _ in range(K):
    num, dir = map(int, input().split())
    # 회전해야 할 톱니바퀴를 큐에 담아서 한 번에 처리한다.
    q.append((num, dir))
    check_left(num, dir)
    check_right(num, dir)
    while q:
        num, dir = q.popleft()
        gear[num - 1] = rotation(gear[num - 1], dir)
score = 0
# 회전이 모두 끝난 뒤 각 기어의 12시를 검사하여 점수를 추가한다.
for n in range(4):
    if gear[n][0] == '0':
        score += 0
    else:
        score += (1 << n)
print(score)