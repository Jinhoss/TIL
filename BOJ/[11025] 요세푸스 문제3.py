import sys
input = sys.stdin.readline

# 점화식으로 구현
# DP는 메모리 초과
N, K= map(int, input().split())
result = 0
for idx in range(2, N + 1):
    result =(result + K) % idx
# 점화식 결과 값이 0-index, 문제는 1-index이므로 +1을 해준다.
print(result + 1)