#퀵정렬
def quick_sort(list):
    if len(list)<=1 : return list
    pivot = list[len(list)//2]
    less_arr, equal_arr, big_arr =[], [], []
    for i in list:
        if i < pivot : less_arr.append(i)
        elif i > pivot : big_arr.append(i)
        else: equal_arr.append(i)
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)
#테스트 케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    customer = list(map(int,input().split()))
    #손님이 도착하는 시간 정렬
    customer = quick_sort(customer)
    cnt = 0
    result = 1
    #손님이 도착했을 때의 시간에 붕어빵이 몇 개 존재하는지 파악, 0개 이하로 있다면 팔 수가 없다.
    for t in customer:
        b = (t//M)*K
        if b-cnt<=0:
            result=0
            break
        else:
            cnt+=1
    if result:
        print('#{} Possible'.format(tc))
    else:
        print('#{} Impossible'.format(tc))