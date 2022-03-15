def evaluation(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    average = []
    arr = [x for x in zip(*scores)]
    length = len(arr)
    for i in range(length):
        min_val = 100
        max_val = 0
        score_dict = {}
        for score in arr[i]:
            score_dict[score] = score_dict.get(score, 0) + 1
            if score > max_val:
                max_val = score
            if score < min_val:
                min_val = score
        if (arr[i][i] == max_val) or (arr[i][i] == min_val):
            if score_dict[arr[i][i]] == 1:
                average.append((sum(arr[i]) - arr[i][i]) / (length - 1))
            else:
                average.append(sum(arr[i])/length)
        else:
            average.append(sum(arr[i])/length)
            
    result = [evaluation(x) for x in average]
    return ''.join(result)
    