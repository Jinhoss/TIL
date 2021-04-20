import sys

def a_BF(v):
    if v == len(a_Arr):
        tmpArr = []
        for i in range(len(a_Arr)):
            if a_ch[i] == 1:
                tmpArr.append(a_Arr[i])
        a_sumArr.append(sum(tmpArr))
    else:
        a_ch[v] = 1
        a_BF(v + 1)
        a_ch[v] = 0
        a_BF(v + 1)


def b_BF(v):
    if v == len(b_Arr):
        tmpArr = []
        for i in range(len(b_Arr)):
            if b_ch[i] == 1:
                tmpArr.append(b_Arr[i])
        b_sumArr.append(sum(tmpArr))
    else:
        b_ch[v] = 1
        b_BF(v + 1)
        b_ch[v] = 0
        b_BF(v + 1)


def upper_bound(start, end, target):
    global cnt

    while start < end:
        mid = (start + end) // 2
        if b_sumArr[mid] <= target:
            start = mid + 1
        else:
            end = mid

    return end


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().split())
    inputArr = list(map(int, sys.stdin.readline().strip().split()))
    cnt = 0

    a_Arr = inputArr[: len(inputArr) // 2]
    b_Arr = inputArr[len(inputArr) // 2:]

    a_sumArr = []
    b_sumArr = []
    a_ch = [0] * (len(a_Arr))
    b_ch = [0] * (len(b_Arr))

    a_BF(0)
    b_BF(0)

    a_sumArr.sort()
    b_sumArr.sort()

    for i in a_sumArr:
        if C - i < 0:
            continue
        else:
            ans = upper_bound(0, len(b_sumArr), C - i)
            cnt += ans

    print(cnt)