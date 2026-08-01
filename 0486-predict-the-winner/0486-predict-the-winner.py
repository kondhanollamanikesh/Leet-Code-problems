class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(i, j):

            if i == j:
                return nums[i]

            pick_left = nums[i] - dfs(i + 1, j)
            pick_right = nums[j] - dfs(i, j - 1)

            return max(pick_left, pick_right)

        return dfs(0, len(nums) - 1) >= 0