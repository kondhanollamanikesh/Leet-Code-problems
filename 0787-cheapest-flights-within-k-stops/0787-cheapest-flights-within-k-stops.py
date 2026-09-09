class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_lst=[[] for _ in range(n)]
        for u,v,w in flights:
            adj_lst[u].append([v,w])
        priority_queue=[]
        priority_queue.append([0,src,0])
        distance=[sys.maxsize for _ in range(n)]
        distance[src]=0
        while len(priority_queue)!=0:
            stop,Node,dist=priority_queue.pop(0)
            for adj_node,weight in adj_lst[Node]:
                if stop>k:
                    continue
                dist_trav=dist+weight
                if dist_trav<distance[adj_node] and stop<=k:
                    distance[adj_node]=dist_trav
                    priority_queue.append([stop+1,adj_node,dist_trav])
        if distance[dst]==sys.maxsize:
            return -1
        return distance[dst]
                