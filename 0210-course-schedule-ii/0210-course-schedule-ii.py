class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees=[0]*numCourses
        adj_mat = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj_mat[v].append(u)
            indegrees[u]+=1
        queue=deque()
        result=[]
        for i in range(0,numCourses):
            if indegrees[i]==0:
                queue.append(i)
        while len(queue)!=0:
            current_node=queue.popleft()
            result.append(current_node)
            for adjmode in adj_mat[current_node]:
                indegrees[adjmode]-=1
                if indegrees[adjmode]==0:
                    queue.append(adjmode)
        if len(result) == numCourses:
            return result

        return []