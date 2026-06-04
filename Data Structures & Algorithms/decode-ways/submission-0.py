class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s)+1)

        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if i < len(s)-1 and 10<=int(s[i]+s[i+1]) <= 26:
                dp[i]+= dp[i+2]
        print(dp)
        return dp[0]