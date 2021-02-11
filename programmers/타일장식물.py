def solution(N):
    lst=[4,6]
    while len(lst)<N:
        lst.append(lst[-1]+lst[-2])
    return lst[-1]