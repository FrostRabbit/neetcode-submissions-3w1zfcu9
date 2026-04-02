class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        res = 0
        leftm = height[start]
        rightm = height[end]
        while start<end:
            if leftm < rightm:
                start+=1
                leftm=max(height[start],leftm)
                res += leftm - height[start]
            else:
                end-=1
                rightm=max(height[end],rightm)
                res += rightm - height[end]

        return res