T = int(input())
for tc in range(1, T+1):
    d, a, b, f = map(int, input().split())
    result = (d/(a+b))*f
    print('#%d %0.6f'%(tc, result))

