import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        l, r = 0, len(nums) - 1
        while l<=r:
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            
            pivot = nums[r]
            p = l
            for i in range(l,r):
                if nums[i] < pivot:
                    nums[p],nums[i] = nums[i], nums[p]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]

            if p > k:
                r = p-1
            elif p<k:
                l=p+1
            else: return nums[p]
        return -1