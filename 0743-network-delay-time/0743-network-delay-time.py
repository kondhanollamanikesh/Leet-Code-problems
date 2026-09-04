class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_lst=[[] for _ in range(n+1)]
        for u,v,w in times:
            adj_lst[u].append([v,w])
        priority_queue=[]
        priority_queue.append([0,k])
        dist=[sys.maxsize for _ in range(n+1)]
        dist[k]=0
        while len(priority_queue)!=0:
            wt,node=heapq.heappop(priority_queue)
            for adj_node,dis in adj_lst[node]:
                dist_trav=wt+dis
                if dist_trav<dist[adj_node]:
                    dist[adj_node]=dist_trav
                    heapq.heappush(priority_queue,[dist_trav,adj_node])
        for i in range(1, n + 1):
            if dist[i] == sys.maxsize:
                return -1

        return max(dist[1:])