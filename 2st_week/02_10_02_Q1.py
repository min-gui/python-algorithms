class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        cur = self.head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next

        cur = self.head
        cur_index = 0;
        while cur is not None:
            if(cur_index == length - k):
                return cur
            cur = cur.next
            cur_index += 1
        return cur

    def get_kth_node_from_last_v2(self, k):
        # 구현해보세요!
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)


print(linked_list.get_kth_node_from_last(1).data)  # 7이 나와야 합니다!