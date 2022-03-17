class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    # Node 인덱스 알아내기
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    # 삽입
    def add_node(self, index, data):
        new_node = Node(data)
        if index==0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    # 삭제 
    def delete_node(self, index):
        if index==0:
            self.head = self.head.next
            return

        node = self.get_node(index - 1)
        node.next = node.next.next


        
