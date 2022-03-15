T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    len_a = len(a)
    len_b = len(b)
    i = 0
    key = 0
    #a를 타이핑하며 b의 첫글자와 같은 글자가 나오면 b의 길이만큼 잘라서 b와 같은지 확인
    #같다면 입력값 1을 증가시키고 다음 입력 글자를 b의 길이만큼 넘어간다
    #아니라면 입력값 1을 증가시키고 다음 글자를 확인
    while i < len_a:
        if a[i] == b[0]:
            if a[i:i+len_b] == b:
                key += 1
                i += len_b
            else:
                key += 1
                i += 1
        else:
            key += 1
            i += 1
    print('#{} {}'.format(tc,key))
