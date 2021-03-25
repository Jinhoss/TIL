from math import gcd
s = input()
t = input()

l_s, l_t = len(s), len(t)
lcm = (l_s * l_t) // gcd(l_s, l_t)

s *= lcm // l_s
t *= lcm // l_t

if s == t:
    print(1)
else:
    print(0)