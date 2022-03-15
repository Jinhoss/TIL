import re
from collections import Counter

def multiSet(string):
    lst = []
    # 두 글자씩 체크하며 다중집합 생성
    for idx in range(len(string)-1):
        if re.match('[a-z]{2}', string[idx:idx+2]):
            lst.append(string[idx:idx+2])
    return lst

def solution(str1, str2):
    # 소문자 변환
    str1=str1.lower()
    str2=str2.lower()
    # 다중집합 생성
    multi_x = multiSet(str1)
    multi_y = multiSet(str2)
    # 다중집합은 중복을 허용함, Counter.elements를 이용하여 intersection
    set_x = Counter(multi_x)
    set_y = Counter(multi_y)
    int_set = list((set_x & set_y).elements())
    
    len_int = len(int_set)
    len_union = len(multi_x)+len(multi_y) - len_int
    if len(set_x) == 0 and len(set_y) == 0:
        return 65536
    if len_union == 0:
        return 65536
    return int(len_int/len_union * 65536)