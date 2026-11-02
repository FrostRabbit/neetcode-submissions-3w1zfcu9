class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3): return False
        if len(s1)<len(s2):
            s1,s2=s2,s1
        n, m = len(s1), len(s2)

        dp = [False] * (m+1)

        dp[0] = True

        for i in range(n+1):
            for j in range(m+1):
                if i > 0:
                    dp[j] &= s1[i-1] == s3[i+j-1] 
                if j > 0:
                    dp[j] |= dp[j-1] and s2[j-1] == s3[i+j-1] 
        return dp[m]