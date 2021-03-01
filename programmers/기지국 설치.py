def solution(n, s, w):
    answer=0
    idx = 0
    locate = 1
    while locate <=n:
        if idx < len(s) and locate >= s[idx]-w:
            locate = s[idx]+w+1
            idx+=1
        else:
            locate += 2*w+1
            answer+=1
    return answer