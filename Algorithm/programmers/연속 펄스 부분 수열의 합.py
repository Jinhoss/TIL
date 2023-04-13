def solution(sequence):
    l = len(sequence)
    prefix_sum = [[0] * (l+1) for _ in range(2)]
    for i in range(l):
        if i%2:
            prefix_sum[0][i+1] = prefix_sum[0][i] - sequence[i]
            prefix_sum[1][i+1] = prefix_sum[1][i] + sequence[i]
        else:
            prefix_sum[1][i+1] = prefix_sum[1][i] - sequence[i]
            prefix_sum[0][i+1] = prefix_sum[0][i] + sequence[i]
    return max(max(prefix_sum[0]) - min(prefix_sum[0]), max(prefix_sum[1]) - min(prefix_sum[1]))