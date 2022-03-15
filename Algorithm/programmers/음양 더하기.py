def solution(absolutes, signs):
    ans = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            ans += num
        else:
            ans -= num
    return ans