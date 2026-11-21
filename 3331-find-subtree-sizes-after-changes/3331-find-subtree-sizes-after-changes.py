class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = [[] for _ in range(n)]

        # Build original tree
        for i in range(1, n):
            p = parent[i]
            tree[p].append(i)

        # Store modified parents
        new_parent = parent[:]

        last = {}

        def dfs(node):
            ch = s[node]

            # Find closest ancestor with the same character
            if ch in last:
                new_parent[node] = last[ch]

            # Save current node as the closest ancestor
            old = last.get(ch)
            last[ch] = node

            for child in tree[node]:
                dfs(child)

            # Backtrack
            if old is None:
                del last[ch]
            else:
                last[ch] = old

        dfs(0)

        # Build modified tree
        new_tree = [[] for _ in range(n)]

        for i in range(1, n):
            new_tree[new_parent[i]].append(i)

        # Calculate subtree sizes
        answer = [1] * n

        def calculate(node):
            for child in new_tree[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer


        