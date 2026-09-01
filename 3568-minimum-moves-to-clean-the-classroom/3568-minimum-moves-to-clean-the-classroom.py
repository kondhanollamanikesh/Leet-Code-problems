class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find starting position and assign an index to every litter
        litter = {}
        start = None

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        # If there is no litter, no moves are needed
        if not litter:
            return 0

        # All litter collected mask
        all_mask = (1 << len(litter)) - 1

        # BFS state:
        # (row, col, remaining_energy, mask, moves)
        queue = deque()
        queue.append((start[0], start[1], energy, 0, 0))

        # visited[row][col][energy][mask]
        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        while queue:

            r, c, curr_energy, mask, moves = queue.popleft()

            # Have we collected every litter?
            if mask == all_mask:
                return moves

            # If no energy, we cannot make another move
            if curr_energy == 0:
                continue

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Check boundaries
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Cannot enter obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Moving costs 1 energy
                new_energy = curr_energy - 1

                # If we reach reset area, restore energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Update litter mask
                new_mask = mask

                if (nr, nc) in litter:
                    litter_index = litter[(nr, nc)]
                    new_mask |= (1 << litter_index)

                # New BFS state
                state = (nr, nc, new_energy, new_mask)

                if state not in visited:
                    visited.add(state)

                    queue.append(
                        (nr, nc, new_energy, new_mask, moves + 1)
                    )

        return -1