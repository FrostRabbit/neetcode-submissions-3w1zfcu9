class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        count = {}
        for n in nums:
            count[n] = 1+count.get(n,0)
        for a,b in count.items():
            bucket[b].append(a)
        result = []
        
        for i in range(len(bucket)-1,0,-1):
            
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result