# import sys
# sys.stdin=open("special_input.txt")

#인풋 입력
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    #idx홀짝에 따라 큰값을 정렬할지 작은값을 정렬할지 결정
    #홀수번째, 즉 리스트 인덱스 number가 짝수일 때는 큰 값이 오게 정렬
    for i in range(10):
        if not i&1:
            max_idx=i
            for j in range(i+1,N):
                if lst[j]>lst[max_idx]:
                    max_idx=j
            lst[i], lst[max_idx] = lst[max_idx], lst[i]
    #리스트 인덱스 number가 홀수일 때는 작은 값이 오도록 정렬
        else:
            min_idx=i
            for j in range(i+1,N):
                if lst[j]<lst[min_idx]:
                    min_idx=j
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
    #asterisk를 이용하여 출력
    print('#{}'.format(tc),*lst[:10])