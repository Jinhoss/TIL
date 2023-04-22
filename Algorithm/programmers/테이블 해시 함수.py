def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x:(x[col-1], -x[0]))
    answer = 0
    for i in range(row_begin, row_end+1):
        idx = i - 1
        sum_v = 0
        for x in sorted_data[idx]:
            sum_v += x%i
            
        answer^=sum_v
        
    return answer