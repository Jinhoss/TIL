# import sys
# sys.stdin = open('input.txt')

def check_cont(num_cnt):
    cont = 0
    for i in range(1, 10):
        if num_cnt[i] == 1:
            cont +=1
        else:
            cont = 0
        if cont == 5:
            return i
    return False
def same_num(num_cnt):
    cnts = sorted(num_cnt, reverse = True)
    if cnts[0] == 4:
        return 8
    elif cnts[0] == 3:
        if cnts[1] == 2:
            return 7
        else:
            return 4
    elif cnts[0] == 2:
        if cnts[1] == 2:
            return 3
        else:
            return 2

def find_num(num_cnt, val):
    nums = []
    for i in range(9, 0, -1):
        if num_cnt[i] == val:
            nums.append(i)
    return nums

num_cnt = [0] * 10
color_lst = {}

for _ in range(5):
    color, num = input().split()
    color_lst[color] = color_lst.get(color, []) + [num]
    num_cnt[int(num)]+=1

flush = False

if len(color_lst) == 1:
    flush = True

score = 0
same = same_num(num_cnt)
if flush and check_cont(num_cnt):
    print(900 + check_cont(num_cnt))
elif same == 8:
    print(800 + num_cnt.index(4))
elif same == 7:
    print(700 + 10*num_cnt.index(3) + num_cnt.index(2))

elif flush:
    print(600 + find_num(num_cnt, 1)[0])

elif check_cont(num_cnt):
    print(500 + find_num(num_cnt, 1)[0])

elif same == 4:
    print(400 + num_cnt.index(3))

elif same == 3:
    nums = find_num(num_cnt, 2)
    print(300 + nums[0] * 10 + nums[1])
elif same == 2:
    print(200 + num_cnt.index(2))

else:
    print(100 + find_num(num_cnt, 1)[0])



