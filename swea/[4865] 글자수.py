T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    max_v=0
    #다소 비효율적인 것 같지만 str1의 글자가 str2에 몇개 있는지 센 후에 최대값과 비교하여 저장
    for s1 in str1:
        cnt = 0
        for s2 in str2:
            if s1 == s2:
                cnt+=1
        if cnt > max_v:
            max_v = cnt
    print('#{} {}'.format(tc,max_v))