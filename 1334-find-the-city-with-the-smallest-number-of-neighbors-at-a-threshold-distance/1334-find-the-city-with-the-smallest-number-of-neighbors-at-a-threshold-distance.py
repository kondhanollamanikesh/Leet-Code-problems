class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_lst = [[] for _ in range(n)]

        for u, v, w in edges:
            adj_lst[u].append([v, w])
            adj_lst[v].append([u, w])

        # 2D distance matrix
        dist = [[sys.maxsize for _ in range(n)] for _ in range(n)]

        # Distance from a city to itself = 0
        for i in range(n):
            dist[i][i] = 0

        # Fill direct edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):

                    if dist[i][k] != sys.maxsize and dist[k][j] != sys.maxsize:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][k] + dist[k][j]
                        )

        # Find city with minimum reachable neighbors
        result = -1
        min_count = sys.maxsize

        for i in range(n):
            count = 0

            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            # >= makes us choose the larger index in case of tie
            if count <= min_count:
                min_count = count
                result = i

        return result