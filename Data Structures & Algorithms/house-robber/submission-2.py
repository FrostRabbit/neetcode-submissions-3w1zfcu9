class Solution:
    def rob(self, nums: List[int]) -> int:
        pre,cur=0,0
        for n in nums:
            temp = max(pre+n,cur)
            pre = cur
            cur = temp
        return cur
