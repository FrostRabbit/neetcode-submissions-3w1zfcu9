class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            a = abs(num)-1
            if nums[a]<0:
                return abs(num)
            nums[a]*=-1
        return -1