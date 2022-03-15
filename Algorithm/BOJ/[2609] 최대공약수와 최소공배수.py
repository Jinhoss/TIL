n, m = map(int, input().split())
multi = n * m
gcd = 0
while True:
    r = n%m
    if r == 0:
        gcd = m
        break
    n = m
    m = r
print(gcd)
print(multi //gcd)
