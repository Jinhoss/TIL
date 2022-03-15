import sys
sys.stdin = open('input.txt')

class Tree:
    def __init__(self):
        self.lst = [0]
    def sort(self, num):
        if num >= 2:
            if self.lst[num] < self.lst[num//2]:
                self.lst[num], self.lst[num//2] = self.lst[num//2], self.lst[num]
                self.sort(num//2)

    def append(self, data):
        num = len(self.lst)
        self.lst.append(data)
        self.sort(num)

    def my_sum(self, node):
        if node <= 1:
            return self.lst[node]
        else:
            return self.lst[node] + self.my_sum(node//2)

    def my_result(self):
        last = len(self.lst) - 1
        self.sum = 0
        if last >= 2:
            return self.my_sum(last//2)
        else:
            return 0

T = int(input())
for tc in range(1, T + 1):
    input()
    tree = Tree()
    for i in map(int, input().split()):
        tree.append(i)
    print('#{} {}'.format(tc, tree.my_result()))