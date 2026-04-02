class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ=n
        for i in range(n):
            summ += i - nums[i]
        return summ