from collections import defaultdict
from bisect import bisect_left, bisect_right


def count_by_lange(lst, start, end):
    return bisect_right(lst, end) - bisect_left(lst, start)

# 와일드카드를 a, z로 대체한 문자로 바꿔서 그 사이에 있는 문자들을 찾는다.
# 예를 들어 fro??같은 경우에는 froaa와 frozz 사이의 값이 되겠다.
# 위와 같은 탐색 방법을 적용하기 위해서는 문자들을 길이 별로 모아서 정렬할 필요가 있다.
def solution(words, queries):
    answer = []
    cands = defaultdict(list)
    reverse_cands = defaultdict(list)
    # 단어를 길이별로 저장
    for word in words:
        cands[len(word)].append(word)
        reverse_cands[len(word)].append(word[::-1])

    # 정렬 => O(NlogN)
    for cand in cands.values():
        cand.sort()
    for cand in reverse_cands.values():
        cand.sort()
    # 탐색 O(N * logM)
    for query in queries:
        # 와일드카드가 접두사인 경우
        if query[0] == '?':
            lst = reverse_cands[len(query)]
            start, end = query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')
        else: # 와일드카드가 접미사인 경우
            lst = cands[len(query)]
            start, end = query.replace('?', 'a'), query.replace('?', 'z')
        answer.append(count_by_lange(lst, start, end))

    return answer