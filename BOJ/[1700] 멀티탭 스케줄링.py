N, K = map(int, input().split())
schedule = list(map(int, input().split()))
plug = []
cnt = 0
for idx in range(K):
    if schedule[idx] in plug:
        continue
    if len(plug) < N:
        plug.append(schedule[idx])
        continue

    i_lst = []
    for j in range(N):
        try:
            i = schedule[idx:].index(plug[j])
        except:
            i = 101
        i_lst.append(i)

    plug_out = i_lst.index(max(i_lst))
    del plug[plug_out]
    plug.append(schedule[idx])
    cnt += 1
print(cnt)





