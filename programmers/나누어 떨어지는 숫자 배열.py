def solution(arr, divisor):
    a=sorted([x for x in arr if x%divisor==0])
    if len(a)==0:
        return [-1]
    else:
        return a

 