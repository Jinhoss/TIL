def time_transform(time):
    lst = time.split(' ')
    end = lst[1]
    duration = lst[2]
    
    lst2= end.split(':')
    # 시간이 소수 셋째 자리까지 표현이 되어있으므로 1000을 곱해서 정수로 표현
    hour = int(lst2[0]) * 1000
    minute = int(lst2[1]) * 1000
    sec = int(lst2[2][0:2] + lst2[2][3:])
    micsec = hour * 3600 + minute * 60 + sec
    lst3 = duration[:-1].split('.')
    if len(lst3) > 1:
        duration2 = int(lst3[0]) * 1000 + int(lst3[1].ljust(3, '0'))
    else: 
        duration2 = int(lst3[0]) * 1000
    
    return [micsec - duration2 + 1, micsec]
# 로그의 처음과 끝 시간과 비교하여 count
def checkProcessNum(time, lst):
    num = 0
    start = time
    end = time + 1000
    for duration in lst:
        if not (duration[1] < start or duration[0] >= end):
            num += 1
    return num

def solution(lines):
    lst = []
    count = []
    # 시간을 변환한 후 lst에 담음
    for string in lines:
        lst.append(time_transform(string))
    # 각 시간대마다 갯수를 count에 담음
    for i in lst:    
        count.append(checkProcessNum(i[0], lst))
        count.append(checkProcessNum(i[1], lst))
    return max(count)