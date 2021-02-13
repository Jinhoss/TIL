from itertools import *
def solution(nums):
    answer = []
    n=len(nums)//2
    
    if len(set(nums))<n:
        return len(set(nums))
    else:
        return n