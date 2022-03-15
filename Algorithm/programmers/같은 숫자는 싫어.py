def solution(arr):
    answer = []
    n=len(arr)
    for i in range(n):
        if i==0:
            answer.append(arr[i])
        elif arr[i]!=arr[i-1]:
            answer.append(arr[i])
    return answer