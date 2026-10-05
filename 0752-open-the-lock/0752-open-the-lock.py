class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        initial_state="0000"
        count=0
        i=0
        if initial_state in deadends:
            return -1
        queue = deque([(initial_state, 0)])
        visited=set(deadends)
        visited.add(initial_state)
        while queue:
            state, count=queue.popleft()
            if state==target:
                return count
            for i in range(4):
                digit = int(state[i])
                next_digit=(digit+1)%10
                next_state=state[:i]+str(next_digit)+state[i+1:]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, count + 1))
                next_digit=(digit-1)%10
                next_state=state[:i]+str(next_digit)+state[i+1:]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, count + 1))
        return -1