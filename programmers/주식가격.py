def solution(prices):
    answer = []
    l=len(prices)
    for i in range(l-1):
        count=0
        for j in range(i+1,l):
            if prices[i]<=prices[j]:
                count+=1
            else:
                count+=1
                break
        answer.append(count)
    answer.append(0)
    return answer