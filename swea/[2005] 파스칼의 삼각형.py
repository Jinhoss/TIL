#테스트케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    #파스칼의 삼각형 값을 담을 배열 생성
    arr = [[0] * n for _ in range(n)]
    #양 끝에는 값을 1, 중앙 값은 위의 값의 합을 받는다.
    for i in range(n):
        for j in range(i+1):
            if j ==0 or j==i:
                arr[i][j]=1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    #한 줄씩 출력
    print('#{}'.format(tc))
    #0이 아닌 값들만 출력
    for lst in arr:
        result = [x for x in lst if x]
        print(*result)



