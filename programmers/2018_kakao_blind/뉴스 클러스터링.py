import re
from collections import Counter as cs
p = re.compile("[a-z]{2}")
def multiSet(str):
    lst = []
    for idx in range(len(str)-1):
        if p.match(str[idx:idx+2]):
            lst.append(str[idx:idx+2])
    return lst
def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    re_x=multiSet(str1)
    re_y=multiSet(str2)
    set_x=cs(re_x)
    set_y=cs(re_y)
    int_set=list((set_x&set_y).elements())
    
    len_int=len(int_set)
    len_union=len(re_x)+len(re_y)-len_int
    if len(set_x)==0 and len(set_y)==0:
        return 65536
    if len_union==0:
        return 65536
    return int(len_int/len_union*65536)