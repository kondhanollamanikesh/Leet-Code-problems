class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V=len(graph)
        adj_lst=[[] for _ in range(V)]
        indegrees=[0]*V
        for node in range(V):
            for adj_node in graph[node]:
                adj_lst[adj_node].append(node)
                indegrees[node]+=1
        queue=deque()
        result=[]
        for i in range(0,V):
            if indegrees[i]==0:
                queue.append(i)
        while len(queue)!=0:
            current_node=queue.popleft()
            result.append(current_node)
            for adjmode in adj_lst[current_node]:
                indegrees[adjmode]-=1
                if indegrees[adjmode]==0:
                    queue.append(adjmode)
        return sorted(result)