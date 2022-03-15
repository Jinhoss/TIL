# 인풋 입력
T = int(input())
for tc in range(1, T + 1):
    l = int(input())
    # 숫자카드를 리스트에 담음
    lst = list(input())
    # 리스트를 돌며 각 카드의 개수를 카운트
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # 어떤 카드가 제일 많은지 조사, 개수가 똑같다면 숫자가 큰 것으로 저장
    max_val = 0
    max_key = 0
    for key, val in dic.items():
        if val > max_val:
            max_key = key
            max_val = val
        elif val == max_val:
            if key > max_key:
                max_key = key
                max_val = val
    # 출력
    print('#{} {} {}'.format(tc, max_key, max_val))
