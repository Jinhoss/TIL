# import sys
# sys.stdin = open('input.txt')

T = int(input())
N =  3162 # 10000000**0.5 약 3162
#에라토스테네스의 체를 이용하여 소수값들을 저장
prime_lst=[False]*2 + [True]*(N-1)
prime=[]
for i in range(2, N+1):
    if prime_lst[i]:
        prime.append(i)
        for idx in range(i*2, N+1, i):
            prime_lst[idx] = False
answer=[]
for tc in range(1, T+1):
    n = int(input())
    result = 1
    #입력값 자체로 제곱수인지 판단
    if n**0.5 != int(n**0.5):
        for p in prime:
            cnt=0
            #갯수가 홀수인 소인수를 곱해준다.
            while not n%p:
                n=n//p
                cnt+=1
            if cnt%2:
                result*=p
            if n==1 or p>n:
                break
        if n>1:
            result*=n
    #이 부분에서 시간이 오래 걸린다는걸 전혀 인지못하고 있었음..
    #테스트 케이스가 10만개라 pirnt함수로 하나하나 출력하는데도 시간이 많이 소요됨
    #리스트에 담아 한 번에 출력하면 시간을 단축시킬 수 있다.
    answer.append('#{} {}'.format(tc, result))
    for ans in answer:
        print(ans)
