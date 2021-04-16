T = int(input())
for tc in range(1, T + 1):
    change = [0] * 8
    money = int(input())
    change_dict = {0:50000, 1:10000, 2:5000, 3:1000, 4:500, 5:100, 6:50, 7:10}
    for i in range(8):
        if money >= change_dict[i]:
            q, money = divmod(money, change_dict[i])
            change[i] += q
    print('#{}'.format(tc))
    print(*change)