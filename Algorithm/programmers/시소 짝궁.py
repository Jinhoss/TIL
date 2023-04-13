def solution(weights):
    weight_dict = {}
    for weight in weights:
        weight_dict[weight] = weight_dict.get(weight, 0) + 1
    weight_lst = sorted(weight_dict.keys())
    l = len(weight_lst)
    result = 0
    for i in range(l-1):
        for j in range(i+1, l):
            w1 = weight_lst[i]
            w2 = weight_lst[j]
            if w2/w1 in [1/1, 2/1, 4/3, 3/2]:
                result += weight_dict[w1] * weight_dict[w2]
    for k, v in weight_dict.items():
        if v>=2:
            result += (v * (v-1))//2
    return result