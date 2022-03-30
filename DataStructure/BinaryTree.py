from pip import main


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self) -> None:
        self.root = None

    # 전위 순회
    def preorder(self, node):
        print(node, end = '')
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)
    # 중위 순회
    def inorder(self, node):
        if node.left is not None:
            self.inorder(node.left)
        print(node, end='')
        if node.right is not None:
            self.inorder(node.right)
    
    # 후위 순회
    def postorder(self, node):
        if node.left is not None:
            self.postorder(node.left)
        if node.right is not None:
            self.postorder(node.right)
        print(node, end='')

    def makeRoot(self, node, left=None, right=None):
        if self.root is  None:
            self.root = node
        node.left = left
        node.right = right

if __name__ == "__main__":
    node = []
    node.append(Node('-'))
    node.append(Node('*'))
    node.append(Node('/'))
    node.append(Node('A'))
    node.append(Node('B'))
    node.append(Node('C'))
    node.append(Node('D'))

    m_tree = Tree()
    for i in range(int(len(node)/2)):
        m_tree.makeRoot(node[i],node[i*2+1],node[i*2+2])

    print(       '전위 순회 : ', end='') ; m_tree.preorder(m_tree.root)
    print('\n' + '중위 순회 : ', end='') ; m_tree.inorder(m_tree.root)
    print('\n' + '후위 순회 : ', end='') ; m_tree.postorder(m_tree.root)