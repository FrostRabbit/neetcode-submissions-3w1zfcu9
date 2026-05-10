class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [s*-1 for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))
            if x > y:
                heapq.heappush(stones,(x-y)*-1)
        if len(stones) == 0:
            return 0
        else:
            return abs(stones[0])