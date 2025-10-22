from typing import List


class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        cnt = 0
        for idx in range(len(points) - 1):
            for idx2 in range(idx + 1, len(points)):
                if self.checkLineOrRectangle(points[idx], points[idx2], points):
                    cnt += 1
        print(cnt)

    def checkLineOrRectangle(self, item1, item2, points):

        # x 비교
        if (item1[0] > item2[0] & item1[1] < item2[1]):
            for point in points:
                if item1[0] > point[0] > item2[0]:
                    return False
                if item1[1] < point[1] < item2[1]:
                    return False
            return True
        #
        if (item1[0] < item2[0] & item1[1] > item2[1]):
            for point in points:
                if item1[0] < point[0] < item2[0]:
                    return False
                if item1[1] > point[1] > item2[1]:
                    return False
            return True
        # x 축이 같으면 y가 달라야 일직선
        if (item1[0] == item2[0]):
            if (item1[1] != item2[1]):
                return True
        # y 축이 같으면 x가 달라야 일직선
        if (item1[1] == item2[1]):
            if (item1[0] != item2[0]):
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    solution.numberOfPairs([[6, 2], [4, 4], [2, 6]])
    solution.numberOfPairs([[3, 1], [1, 3], [1, 1]])
    solution.numberOfPairs([[1, 1], [2, 2], [3, 3]])
