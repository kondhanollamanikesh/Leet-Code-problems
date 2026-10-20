class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)

        max_freq = max(freq.values())

        count_max = 0
        for value in freq.values():
            if value == max_freq:
                count_max += 1

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + count_max
        )