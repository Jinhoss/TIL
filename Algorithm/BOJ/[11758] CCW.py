lst = [list(map(int, input().split())) for _ in range(3)]
lst.append(lst[0])
left = 0
right = 0

for i in range(3):
    left += lst[i][0] * lst[i + 1][1]
    right += lst[i][1] * lst[i + 1][0]

result = left - right

if result > 0:
    print(1)

elif result == 0 :
    print(0)
else:
    print(-1)