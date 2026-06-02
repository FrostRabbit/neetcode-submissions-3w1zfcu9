class Solution:
    def rob(self, nums: List[int]) -> int:
        def repeat(nums):
            pre,cur=0,0
            for n in nums:
                temp = max(pre+n,cur)
                pre = cur
                cur = temp
            return cur
        return max(nums[0],repeat(nums[1:]),repeat(nums[:-1]))