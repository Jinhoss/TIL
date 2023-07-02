import heapq


def time_transform(string):
    hour, minute = string.split(":")
    return int(hour) * 60 + int(minute)


def solution(book_time):
    answer = 0
    q = []
    hotel = []
    heapq.heapify(q)
    for start, end in book_time:
        start, end = time_transform(start), time_transform(end)
        heapq.heappush(q, (start, end))
    while q:
        s, e = heapq.heappop(q)
        if not hotel:
            hotel.append(e)
        else:
            l = len(hotel)
            for i in range(l):
                if hotel[i] <= s:
                    hotel[i] = e
                    break
            else:
                hotel.append(e)
    return len(hotel)


print(solution([["08:00", "08:30"], ["08:00", "13:00"], ["12:30", "13:30"]]))
