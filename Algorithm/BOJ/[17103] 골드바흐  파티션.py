import sys
input = sys.stdin.readline

T = int(input())
N = 1000000
# 테스트 케이스가 여러개이므로 미리 소수 리스트를 작성
# 에스토라테네스의 체
prime = [False]* 2 + [True] * (N -1)
prime_lst = []
for idx in range(2, N):
    if prime[idx]:
        prime_lst.append(idx)
        for i in range(idx*2, N, idx):
            prime[i] = False

for _ in range(T):
    n = int(input())
    idx = 0
    cnt = 0
    while True:
        p = prime_lst[idx]
        if p > n//2:
            break
        # 처음에 n-p in prime_lst를 사용하니 시간초과 발생
        # 체크는 prime으로 확인
        if prime[n-p]:
            cnt+=1
        idx += 1
    print(cnt)
