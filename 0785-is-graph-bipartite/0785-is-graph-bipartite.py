class Solution:
    def dfs(self,current_node,visited,graph,color):
        visited[current_node]=color
        for adj_node in graph[current_node]:
            if visited[adj_node]!=-1:
                if visited[adj_node]==color:
                    return False
            else:
                if color==0:
                    ans=self.dfs(adj_node,visited,graph,1)
                else:
                    ans=self.dfs(adj_node,visited,graph,0)
                if ans==False:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        total_nodes=len(graph)
        visited=[-1]*total_nodes
        for i in range(total_nodes):
            if visited[i]==-1:
                ans=self.dfs(i,visited,graph,0)
                if ans==False:
                    return False
        return True