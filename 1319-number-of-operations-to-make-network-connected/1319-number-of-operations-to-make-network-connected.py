class disjoint_set:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0] * n
    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)

        if pu==pv:
            return True
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        elif self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
        return False

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        ds=disjoint_set(n)
        xtra_edges=0
        for u,v in connections:
            if ds.union(u,v):
                xtra_edges+=1
        ans=0
        for i in range(n):
            if ds.find(i)==i:
                ans+=1
        if xtra_edges>=(ans-1):
            return ans-1
        return -1