from bisect import bisect

for _ in range(int(input())):
    n = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()
    m = int(input())
    note2 = list(map(int, input().split()))
    for num in note2:
        if num == note1[bisect(note1, num) - 1]:
            print(1)
        else:
            print(0)