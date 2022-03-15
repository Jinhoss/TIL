import re

def time_transform(time):
    m_s = time.split(':')
    result = int(m_s[0]) * 60
    result += int(m_s[1])
    return result

def change_code(code):
    code = re.sub('C#', 'c', code)
    code = re.sub('D#', 'd', code)
    code = re.sub('F#', 'f', code)
    code = re.sub('G#', 'g', code)
    code = re.sub('A#', 'a', code)
    return code

def solution(m, musicinfos):
    answer = []
    idx = 0
    for musicinfo in musicinfos:
        m = change_code(m)
        info_split = musicinfo.split(',')
        time = time_transform(info_split[1]) - time_transform(info_split[0])
        check = info_split[3]
        check = change_code(check)
        if time > len(check):
            q, r = divmod(time, len(check))
            check = check * q + check[:r]
        else:
            check = check[:time]
        if m in check:
            answer.append((idx, time, info_split[2]))
        idx += 1
    if answer:
        answer = sorted(answer, key=lambda x: (-x[1], x[0]))
        return answer[0][2]
    return "(None)"