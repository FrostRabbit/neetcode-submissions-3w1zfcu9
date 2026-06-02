class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:return nums[0]
        def repeat(nums):
            pre,cur=0,0
            for n in nums:
                temp = max(pre+n,cur)
                pre = cur
                cur = temp
            return cur
        return max(repeat(nums[1:]),repeat(nums[:-1]))