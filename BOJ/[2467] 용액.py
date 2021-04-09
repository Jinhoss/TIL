N = int(input())
lst = list(map(int, input().split()))
lst.sort()
low, high = 0, N-1
limit = lst[low] + lst[high]
answer1, answer2 = 0, 0
while low < high:
    mix = lst[low] + lst[high]
    if abs(mix) <= abs(limit):
        limit = mix
        answer1 = low
        answer2 = high
        if limit == 0:
            break
    if mix >= 0 :
        high -= 1
    else:
        low += 1
print(lst[answer1], lst[answer2])