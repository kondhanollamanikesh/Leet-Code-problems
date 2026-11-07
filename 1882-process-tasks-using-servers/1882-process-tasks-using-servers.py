class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        busy = []

        for ind, weight in enumerate(servers):
            heapq.heappush(available, (weight, ind))

        res = []
        current_time = 0

        for i in range(len(tasks)):

            current_time = max(current_time, i)

            # Move completed servers into available heap
            while busy and busy[0][0] <= current_time:
                free_time, weight, ind = heapq.heappop(busy)
                heapq.heappush(available, (weight, ind))

            # If no server is available, wait
            if not available:
                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    free_time, weight, ind = heapq.heappop(busy)
                    heapq.heappush(available, (weight, ind))

            # Select the best available server
            weight, ind = heapq.heappop(available)

            res.append(ind)

            # Calculate when this server becomes free
            heapq.heappush(
                busy,
                (current_time + tasks[i], weight, ind)
            )

        return res