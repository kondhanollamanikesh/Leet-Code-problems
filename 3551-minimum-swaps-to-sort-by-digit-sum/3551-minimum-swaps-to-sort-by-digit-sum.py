class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        lst=[]
        for i in nums:
            ans=0
            num=str(i)
            for j in num:
                ans+=int(j)
            lst.append([ans,i])
        lst.sort()
        lst.sort()

        n = len(nums)
        pos = {value: i for i, value in enumerate(nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[lst[i][1]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                value = lst[j][1]
                j = pos[value]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps