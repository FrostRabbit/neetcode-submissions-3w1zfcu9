class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=0
        prod = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] ==0:
                zeros+=1
                z_index = i
            else:
                prod *= nums[i]
        
        if zeros >=2: return res
        if zeros == 1:
            for i in nums:
                if i ==0: break
            res[z_index] = prod
        if zeros == 0:
            for i in range(len(nums)):
                res[i] = int(prod / nums[i])
        return res 
        