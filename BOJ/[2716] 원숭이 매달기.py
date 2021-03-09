# import sys
# sys.stdin = open('input.txt')

# 최대 깊이를 찾는 문제이다.
T = int(input())
for _ in range(T):
    tree = input()
    depth = 0
    max_depth = 0
    # [ 일 때 깊이를 + 1, ]일 때 깊이를 -1 해주면서 최대값을 찾는다.
    for x in tree:
        if x == '[':
            depth+=1
        elif x == ']':
            depth-=1
        if depth > max_depth:
            max_depth = depth
    # 최대값만큼 비트 시프트
    print(1<<max_depth)