class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums =[]
        heapq.heapify(nums)
        for x,y in points:
            d = x**2+y**2
            heapq.heappush(nums,[d*-1,x,y])
            if len(nums) > k:
                heapq.heappop(nums)
        results=[]
        while len(nums) > 0:
            r = heapq.heappop(nums)
            results.append([r[1],r[2]])
        return results