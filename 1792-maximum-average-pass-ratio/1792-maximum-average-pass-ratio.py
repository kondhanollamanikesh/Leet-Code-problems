class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        heap = []

        for i, (pass1, total) in enumerate(classes):
            avg = (pass1 + 1) / (total + 1) - pass1 / total
            heapq.heappush(heap, (-avg, pass1, total))

        for _ in range(extraStudents):
            avg, pass1, total = heapq.heappop(heap)

            pass1 += 1
            total += 1

            new_avg = (pass1 + 1) / (total + 1) - pass1 / total
            heapq.heappush(heap, (-new_avg, pass1, total))

        final = 0

        for avg, pass1, total in heap:
            final += pass1 / total

        totalavg = final / len(classes)
        return totalavg
