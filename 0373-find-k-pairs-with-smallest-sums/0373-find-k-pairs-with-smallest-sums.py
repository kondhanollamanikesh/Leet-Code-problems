class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        prior = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(prior, (nums1[i] + nums2[0], i, 0))

        result = []

        while prior and len(result) < k:
            total, i, j = heapq.heappop(prior)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(prior, (nums1[i] + nums2[j + 1], i, j + 1))

        return result