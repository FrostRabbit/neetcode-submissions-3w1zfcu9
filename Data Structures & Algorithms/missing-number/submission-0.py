class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        sumt = int(n*(n+1) / 2)
        for num in nums:
            summ += num
        return sumt-summ