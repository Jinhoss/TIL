def solution(lottos, win_nums):
    joint = list(set(lottos) & set(win_nums))
    rank1 = min(7 - len(joint), 6)
    zero = len([i for i in lottos if not i])
    rank2 = min(7 - len(joint) - zero, 6)
    return [rank2, rank1]