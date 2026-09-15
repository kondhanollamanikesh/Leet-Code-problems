class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_lst = [[] for _ in range(n)]

        for u, v, w in edges:
            adj_lst[u].append([v, w])
            adj_lst[v].append([u, w])

        dist = [[sys.maxsize for _ in range(n)] for _ in range(n)]

        set1 = set()

        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):

                    if dist[i][k] != sys.maxsize and dist[k][j] != sys.maxsize:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][k] + dist[k][j]
                        )

        # Your set approach
        for i in range(n):

            list1 = []

            for j in range(n):

                if i != j and dist[i][j] <= distanceThreshold:
                    list1.append(j)

            tuple1 = tuple(list1)

            set1.add((i, tuple1))

        # Find minimum
        minimum = sys.maxsize
        result = -1

        for city, neighbors in set1:

            count = len(neighbors)

            if count < minimum:
                minimum = count
                result = city

            elif count == minimum and city > result:
                result = city

        return result