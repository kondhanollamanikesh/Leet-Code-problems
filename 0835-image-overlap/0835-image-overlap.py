class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        points1 = []
        points2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))

                if img2[i][j] == 1:
                    points2.append((i, j))

        count = {}

        for x1, y1 in points1:
            for x2, y2 in points2:

                dx = x2 - x1
                dy = y2 - y1

                if (dx, dy) not in count:
                    count[(dx, dy)] = 0

                count[(dx, dy)] += 1

        return max(count.values(), default=0)