T = int(input())
for test_case in range(1, 1 + T):
    N, *M = map(int, input().split())
    bus = 0
    bus_battery = M[bus]
    cnt = 0

    while bus + bus_battery < N - 1:
        max_charge = 0
        next_bus = None
        for i in range(bus_battery, 0, -1):
            charge = M[bus + i] - (bus_battery - i)
            if charge > max_charge:
                max_charge = charge
                next_bus = bus + i
        if next_bus is None:
            cnt = -1
        else:
            bus = next_bus
            bus_battery = M[bus]
            cnt += 1

    print('#{} {}'.format(test_case, cnt))