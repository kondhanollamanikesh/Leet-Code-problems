class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(index, curr, total):
            # If we reached the target
            if total == target:
                result.append(curr[:])
                return

            # If total exceeds target or no candidates left
            if total > target or index == len(candidates):
                return

            # Take the current candidate
            curr.append(candidates[index])
            backtrack(index, curr, total + candidates[index])

            # Backtrack
            curr.pop()

            # Skip the current candidate
            backtrack(index + 1, curr, total)

        backtrack(0, [], 0)
        return result