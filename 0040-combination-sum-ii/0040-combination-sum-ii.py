class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Pruning
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # Move to the next index (each number used only once)
                backtrack(i + 1, remaining - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return result