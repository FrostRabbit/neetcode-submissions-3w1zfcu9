class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if sum(nums)%2 != 0: return False
        s = int(sum(nums)/2)
        dp = [False] * (s+1)
        dp[0] = True
        for num in nums:
            for cur in range(s-num,-1,-1):
                if dp[cur]:
                    dp[cur+num] = True
            if dp[s]: return True
        return False