def change_time(time_info):
    lst = list(map(int, time_info.split(':')))
    new_time = lst[0] * 3600 + lst[1] * 60 + lst[2]
    return new_time              

def change_time2(time_info):
    h, r = divmod(time_info, 3600)
    m, s = divmod(r, 60)
    return '%0.2d:%0.2d:%0.2d'%(h, m, s)

def solution(play_time, adv_time, logs):
    answer = ''
    if play_time == adv_time:
        return "00:00:00"
    play_time = change_time(play_time)
    adv_time = change_time(adv_time)               
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:
        start, end = l.split('-')
        start = change_time(start)
        end = change_time(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return change_time2(max_time)