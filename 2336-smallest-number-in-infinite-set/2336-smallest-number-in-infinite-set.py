class SmallestInfiniteSet:

    def __init__(self):
        self.s = set()
        self.lst = []
        self.current = 1

    def popSmallest(self) -> int:
        if len(self.s)!=0:
            val=heapq.heappop(self.lst)
            self.s.remove(val)
            return val
        val = self.current
        self.current += 1
        return val
    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.s:
            heapq.heappush(self.lst, num)
            self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)