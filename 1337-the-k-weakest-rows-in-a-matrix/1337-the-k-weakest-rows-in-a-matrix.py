class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        priority_queue=[]
        for i in range(len(mat)):
            total=sum(mat[i])
            heapq.heappush(priority_queue,[total,i])
        ans=[]
        for i in range(k):
            val,ind=heapq.heappop(priority_queue)
            ans.append(ind)
        return ans