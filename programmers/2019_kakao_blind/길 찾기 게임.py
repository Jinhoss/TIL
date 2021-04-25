import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, data):
        self.data = data
        self.x = self.data[0]
        self.left = None
        self.right = None


def solution(nodeinfo):
    pre_lst = []
    post_lst = []
    answer = []

    def preorder(node):
        pre_lst.append(nodeinfo.index(node.data) + 1)
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

    def postorder(node):
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        post_lst.append(nodeinfo.index(node.data) + 1)

    sorted_info = sorted(nodeinfo, key = lambda x: (-x[1], x[0]))

    root = 0
    for node in sorted_info:
        if not root:
            root = Tree(node)
        else:
            current = root
            while True:
                if node[0] < current.x:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(node)
                        break
                else:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break
                    break
    preorder(root)
    postorder(root)
    answer.append(pre_lst)
    answer.append(post_lst)
    return answer

if __name__ == '__main__':
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))