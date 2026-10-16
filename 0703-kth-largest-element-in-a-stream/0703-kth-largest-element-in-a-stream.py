class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def heapify(self, nums):
        return nums[0]

    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heapify(self.nums)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        ans = self.heapify(self.nums)
        return ans


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)