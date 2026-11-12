class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)<len(word2):
            word1,word2=word2,word1
        n,m = len(word1),len(word2)
        dp = [i for i in range(m+1)]
        for i in range(1,n+1):
            prev = dp[0]
            dp[0] = i
            for j in range(1,m+1):
                top = dp[j]
                if word1[i-1]==word2[j-1]:
                    dp[j] =prev
                else:
                    dp[j] = 1+min(prev,top,dp[j-1])
                prev = top
        return dp[m ]