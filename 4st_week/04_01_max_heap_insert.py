


class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        # 1. 원소를 맨 끝에 추가합니다.
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index != 1: # 1인 경우에는 root node 라 더 비교할 게 없음. 올라갈 일이 없음.
            # 2. 부모 노드랑 비교해서 내가 더 크다면 위치를 바꾼다.
            parent_index = cur_index // 2

            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index] , self.items[parent_index] = self.items[parent_index] , self.items[cur_index]
                cur_index = parent_index
            else:
                break

        #        cur
        # 0   1   2
        # [None, 4, 9]

        #    cur
        # 0   1   2
        # [None, 9, 1]

        return


max_heap = MaxHeap()
max_heap.insert(3)

# 3 Level
# -> [None , 3]
#1. 맨 뒤에다가 원소를 넣는다.
# 2. 부모와 비교해서 자기가 높으면 바꾼다.
# 3.
# 4 level 0
# 3 level 1
# [None, 4, 3]

max_heap.insert(4)
# max_heap.insert(2)
# max_heap.insert(9)

#       4      Level 0
#     3   2    Level 1
#    9         Level 2
# [None, 9, 4, 2, 3]
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!