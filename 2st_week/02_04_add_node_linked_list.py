class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next

        print()

    def get_node(self, index):
        cur = self.head
        cnt = 0
        while cnt != index:
            cur = cur.next
            cnt += 1

        return cur

    def add_node(self, index, value):
        node = Node(value)

        if (index == 0):
            node.next = self.head
            self.head = node
            return


        prev_node = self.get_node(index - 1)
        node_next = prev_node.next
        prev_node.next = node
        node.next = node_next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(5)
linked_list.append(6)
linked_list.add_node(0, 8)

linked_list.print_all()
