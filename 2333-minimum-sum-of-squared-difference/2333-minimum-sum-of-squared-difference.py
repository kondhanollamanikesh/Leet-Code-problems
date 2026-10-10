class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        n = len(diff) - 1

        for i in range(n):
            count = i + 1
            need = (diff[i] - diff[i + 1]) * count

            if k >= need:
                k -= need
            else:
                level = k // count
                remainder = k % count

                for j in range(count):
                    diff[j] = diff[i] - level

                for j in range(remainder):
                    diff[j] -= 1

                k = 0
                break

        if k > 0:
            level = k // n
            remainder = k % n

            for i in range(n):
                diff[i] = max(0, diff[n - 1] - level)

            for i in range(remainder):
                if diff[i] > 0:
                    diff[i] -= 1

        return sum(x * x for x in diff[:n])