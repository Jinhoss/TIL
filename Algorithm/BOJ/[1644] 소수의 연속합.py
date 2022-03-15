prime_lst = [True] * 2 + [False] * 3999999
prime = []
for i in range(2, 4000001):
    if prime_lst[i] == False:
        prime.append(i)
        for idx in range(i * 2, 4000000, i):
            prime_lst[idx] = True

N = int(input())

l = len(prime)
end = 0
sub_sum = 0
result = 0
for i in range(l):
    if prime[i] > N:
        break
    while sub_sum < N and end < l - 1:
        sub_sum += prime[end]
        end += 1
    if sub_sum == N:
        result += 1
    sub_sum -= prime[i]
print(result)
