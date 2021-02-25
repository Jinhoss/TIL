#테스트 케이스 수 입력
T = int(input())
for t in range(1,T+1):
    num = int(input())
    arr = list(map(int,input().split()))
    #역으로 접근하기 위해 배열을 뒤집었다.
    arr = arr[::-1]
    #초기값을 최대값으로 지정
    max_v = arr[0]
    cnt = 0
    #다음값이 저장된 값보다 작으면 수익이 난 것으로 간주
    #이익을 저장
    for i in range(1,len(arr)):
        if max_v > arr[i]:
            cnt += max_v-arr[i]
    #저장된 값보다 크면 최대값 갱신
        else:
            max_v = arr[i]
    print("#{} {}".format(t, cnt))