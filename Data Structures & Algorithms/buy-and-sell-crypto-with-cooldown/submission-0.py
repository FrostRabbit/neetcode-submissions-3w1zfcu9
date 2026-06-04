class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(2):
                if j:
                    b = dp[i+1][0] - prices[i] if i<n-1 else -prices[i]
                    c = dp[i+1][1] if i<n-1 else 0
                    dp[i][1] = max(b,c)
                else:
                    s = dp[i+2][1] + prices[i] if i<n-2 else prices[i]
                    c = dp[i+1][0] if i<n-1 else 0
                    dp[i][0] = max(s,c)
        return dp[0][1]