class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_lst = [[] for _ in range(n)]

        for u, v, w in roads:
            adj_lst[u].append([v, w])
            adj_lst[v].append([u, w])

        queue = []
        heapq.heappush(queue, [0, 0])

        dist = [sys.maxsize] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        MOD = 10**9 + 7

        while queue:
            distance, node = heapq.heappop(queue)

            if distance > dist[node]:
                continue

            for adj_node, w in adj_lst[node]:

                dist_trav = distance + w

                # Found a shorter path
                if dist_trav < dist[adj_node]:
                    dist[adj_node] = dist_trav
                    ways[adj_node] = ways[node]

                    heapq.heappush(queue, [dist_trav, adj_node])

                # Found another shortest path
                elif dist_trav == dist[adj_node]:
                    ways[adj_node] = (ways[adj_node] + ways[node]) % MOD

        return ways[n - 1]