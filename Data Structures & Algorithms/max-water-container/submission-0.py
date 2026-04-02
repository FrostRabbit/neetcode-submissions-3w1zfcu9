class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end =len(heights)-1
        m = 0
        while start<end:
            sh = heights[start]
            se = heights[end]
            m = max(m,(end-start) * min(sh,se))
            if sh > se:
                end -=1
            else: start+=1
        return m