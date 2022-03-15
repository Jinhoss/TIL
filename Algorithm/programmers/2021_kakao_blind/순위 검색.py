from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    db = {}
    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        for n in range(5):
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = conditions[:]
                for v in c:
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]
    for value in db.values():
        value.sort()
    for q in query:
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])

        if qry_cnd in db:
            data = db[qry_cnd]

            if len(data) > 0:
                answer.append(len(data) -  bisect_left(data, qry_score))
        else:
            answer.append(0)
    return answer
