class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast=slow=0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        begin = 0
        while True:
            slow = nums[slow]
            begin = nums[begin]
            if slow == begin:
                return slow