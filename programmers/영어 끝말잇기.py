def solution(n, words):
    answer = []
    check=[words[0]]
    for i in words[1:]:
        if (i not in check) and (i[0]==check[-1][-1]):
            check.append(i)
        else:
            x=len(check)
            return [(x%n)+1,(x//n)+1]
    if len(check)==len(words):
        return [0,0]