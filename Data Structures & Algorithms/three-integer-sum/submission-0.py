class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = defaultdict(int)
        res =[]
        nums.sort()
        for n in nums:
            dic[n] += 1
        
        for i in range(len(nums)):
            dic[nums[i]] -=1
            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,len(nums)):
                dic[nums[j]] -=1
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                su = -(nums[i]+nums[j])
                if dic[su] > 0:
                    res.append([nums[i],nums[j],su])
            for j in range(i+1,len(nums)):
                dic[nums[j]] += 1
        
        return res