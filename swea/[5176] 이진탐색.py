class Tree:
    def __init__(self, N ):
        self.lst = [0] * (N + 1)
        self.N = N
        self.cnt = 1
        self.numbering(1)

    def numbering(self, num):
        if num <= N:
            self.numbering(2 * num)
            self.lst[num] = self.cnt
            self.cnt += 1
            self.numbering(2 * num + 1)

    def my_result(self):
        return ' '.join(map(str, (self.lst[1], self.lst[self.N//2])))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = Tree(N)
    print('#{} {}'.format(tc, tree.my_result()))