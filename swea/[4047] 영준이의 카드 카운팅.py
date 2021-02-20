# import sys
# sys.stdin = open("input.txt")
#카드를 검사하는 함수
def check(card):
    #모양 S, D, H, C 각 13장에 대해 카드가 있는지 중복되는건 없는지 확인하기 위한 check_lst
    check_lst = [[0] * 13 for _ in range(4)]
    idx = 0
    l = len(card)
    #input에서 받은 알파벳으로 check_lst 행 위치를 결정
    dic = {'S': 0, 'D': 1, 'H': 2, 'C': 3}
    while idx < l:
        #카드모양에 따른 행 위치 결정
        shp = dic[card[idx]]
        # 숫자값이 1~13이므로 idx값을 0~12로 해주기 위해 num에서는 -1을 해준다
        num = int(card[idx + 1] + card[idx + 2])-1
        #이미 값이 존재하는 경우라면 False를 리턴
        if check_lst[shp][num]:
            return False
        check_lst[shp][num]+=1
        #TXY 3개씩 끊어서 봐야하기 때문에 idx+=3이다
        idx+=3
    #check_lst 배열을 돌며 값이 없는 만큼 카운트해서 반환
    result = [0]*4
    for i in range(4):
        for j in range(13):
            if not check_lst[i][j]:
                result[i] += 1
    return result




T = int(input())
for tc in range(1, T+1):
    card = input()
    result = check(card)
    #check함수를 통해 배열을 반환받았다면 출력해주고, False를 받았다면 ERROR를 출력
    if result:
        print('#{}'.format(tc), *result)
    else:
        print('#{} ERROR'.format(tc))





