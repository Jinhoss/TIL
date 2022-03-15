def solution(table, languages, preference):
    result = {}
    for lst in table:
        scores = {}
        score_lst = list(lst.split())
        for i in range(1, 6):
            lang = score_lst[i]
            scores[lang] = scores.get(lang, 0) + (6 - i)
        
        for pref, score in zip(languages, preference):
            result[score_lst[0]] = result.get(score_lst[0], 0) + scores.get(pref, 0) * score
    return sorted(result.items(), key = lambda x: (-x[1], x[0]))[0][0]