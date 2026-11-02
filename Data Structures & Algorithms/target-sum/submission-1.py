class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            dp_ = defaultdict(int)
            for idx, cnt in dp.items():
                dp_[idx+nums[i]] += cnt
                dp_[idx-nums[i]] += cnt
            dp = dp_

        return dp[target]