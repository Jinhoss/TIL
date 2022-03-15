import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lst = [int(input()) for _ in range(n)]
        lst.sort()
        start, end = 0, n - 1
        check = True
        while start < end:
            l1 = lst[start]
            l2 = lst[end]
            if l1 + l2 == x:
                print('yes', l1, l2)
                check = False
                break
            else:
                if l1 + l2 < x:
                    start += 1
                else:
                    end -=1
        if check:
            print('danger')
    except:
        break