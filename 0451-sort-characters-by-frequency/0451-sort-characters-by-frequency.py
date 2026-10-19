class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map={}
        for i in s:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1
        queue=[]
        for key,value in hash_map.items():
            heapq.heappush(queue,[-value,key])
        final=""
        for _ in range(len(queue)):
            value,key=heapq.heappop(queue)
            final+=key*(-value)
        return final