class Solution:
    def rob(self, nums: List[int]) -> int:
        def repeat(s,e):
            pre,cur=0,0
            for i in range(s,e):
                temp = max(pre+nums[i],cur)
                pre = cur
                cur = temp
            return cur
        return max(nums[0],repeat(1,len(nums)),repeat(0,len(nums)-1))