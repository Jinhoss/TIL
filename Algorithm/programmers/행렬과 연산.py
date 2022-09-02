from collections import deque

def shift(r_lst, c_lst):
    r_lst.appendleft(r_lst.pop())
    c_lst[0].appendleft(c_lst[0].pop())
    c_lst[1].appendleft(c_lst[1].pop())
    return r_lst, c_lst

def rotate(r_lst, c_lst):
    r_lst[0].appendleft(c_lst[0].popleft())
    c_lst[1].appendleft(r_lst[0].pop())
    r_lst[-1].append(c_lst[1].pop())
    c_lst[0].append(r_lst[-1].popleft())
    return r_lst, c_lst
    

def solution(rc, operations):
    r_len = len(rc)
    c_len = len(rc[0])
    row = deque([deque(lst[1:-1]) for lst in rc])
    out_cols = [deque(rc[r][0] for r in range(r_len)), deque(rc[r][c_len-1] for r in range(r_len))]
    for oper in operations:
        if oper == 'ShiftRow':
            row, out_cols = shift(row, out_cols)
        else:
            row, out_cols = rotate(row, out_cols)
            
    answer = []
    for idx in range(r_len):
        new_row = []
        new_row.append(out_cols[0][idx])
        new_row.extend(row[idx])
        new_row.append(out_cols[1][idx])
        answer.append(new_row)
        
    return answer
    