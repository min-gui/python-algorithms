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
            print(cur.data, end= ' ')
            cur = cur.next

        print()


linked_list = LinkedList(8)
linked_list.print_all()
linked_list.append(5)
linked_list.print_all()
linked_list.append(10)
linked_list.print_all()