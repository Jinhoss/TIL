import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[^\w\d\-_.]', '', answer)
    answer = re.sub('\.+', '.', answer)
    answer = re.sub('^[.]|[.]$', '', answer)
    if not answer:
        answer = 'a'
    else:
        answer = answer[:15]
    answer = re.sub('[.]$', '', answer)
    l = len(answer)
    if l <=2 :
        for _ in range(3-l):
            answer+=answer[-1]
    return answer
