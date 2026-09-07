class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices.copy()

        for i in range(len(prices)):

            while stack and prices[i] <= prices[stack[-1]]:
                
                j = stack.pop()

                ans[j] = prices[j] - prices[i]

            stack.append(i)

        return ans