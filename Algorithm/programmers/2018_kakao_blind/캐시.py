def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower()
        if not city in cache:
            if len(cache) < cacheSize:
                cache.append(city)

            elif cache:
                cache.pop(0)
                cache.append(city)
            time += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            time += 1
    return time