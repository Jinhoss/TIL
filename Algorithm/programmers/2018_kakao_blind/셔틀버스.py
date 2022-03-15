def solution(n, t, m, timetable):
    timetable = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable])
    # 모두 분으로 초기화한다.
    last_time = 9 * 60 + (n - 1) * t

    for i in range(n):
        # 탑승인원이 남으면 마지막 시간에 탑승
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        if i == n - 1:
            # 마지막 운행 시간보다 늦은 시간에 대기 => 그 날에 안타므로 무시
            if timetable[0] > last_time:
                return '%02d:%02d' % (last_time // 60, last_time % 60)
            # 마지막 탑승자보다 1분 일찍 탑승
            time = timetable[m - 1] - 1
            return '%02d:%02d' % (time // 60, time % 60)
        # 버스를 운행하며 타는 사람들은 timetable에서 제외한다.
        for j in range(m - 1, -1, -1):
            bus_arrive = 540 + i * t
            cnt = 0
            if timetable[j] <= bus_arrive:
                cnt += 1
            timetable = timetable[cnt:]

