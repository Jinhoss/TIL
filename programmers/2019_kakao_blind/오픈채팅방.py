def solution(record):
    infos = list(map(lambda x: x.split(), record))
    users = {}
    for info in infos:
        if len(info) > 2:
            users[info[1]] = info[2]
    msg = {'Enter':'님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    result = []
    for info in infos:
        if info[0] != 'Change':
            result.append(users[info[1]] + msg[info[0]])
    return result