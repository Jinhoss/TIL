def solution(sequence, k):
    l = len(sequence)
    start = 0
    end = 0
    sum_v = sequence[0]
    max_length = l + 1
    result = []
    if sum_v==k:
        max_length=1
        result = [0, 0]
    while start<l and end<l:
        if sum_v<k:
            end += 1
            if end>=l:
                break
            sum_v += sequence[end]
        elif sum_v>=k:
            if sum_v==k and (end - start + 1<max_length):
                max_length = end - start + 1
                result = [start, end]
            start += 1
            if start>=l or start>end:
                break
            sum_v -= sequence[start-1]
    if not result:
        result = [start, end]
    return result