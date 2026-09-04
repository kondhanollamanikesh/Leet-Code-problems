class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_lst=[[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            adj_lst[u].append((v, succProb[i]))
            adj_lst[v].append((u, succProb[i]))

        priority_queue=[]
        heapq.heappush(priority_queue, (-1, start_node))
        dist = [0.0 for _ in range(n)]
        dist[start_node] = 1.0
        while len(priority_queue)!=0:
            wt,node=heapq.heappop(priority_queue)
            wt = -wt
            for adj_node,dis in adj_lst[node]:
                dist_trav=wt*dis
                if dist_trav>dist[adj_node]:
                    dist[adj_node]=dist_trav
                    heapq.heappush(priority_queue,[-dist_trav,adj_node])
        return dist[end_node]