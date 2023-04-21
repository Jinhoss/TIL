def solution(name, yearning, photo):
    score_dict = {k:v for k, v in zip(name, yearning)}
    result = []
    for name_lst in photo:
        score = 0
        for name in name_lst:
            score += score_dict.get(name, 0)
        result.append(score)
        
    return result
        