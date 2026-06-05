class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pre=intervals[0][1]
        res=0
        for i in range(1,len(intervals)):
            if intervals[i][0] < pre:
                res+=1
                pre= min(pre,intervals[i][1])
            else:
                pre = intervals[i][1]
        return res