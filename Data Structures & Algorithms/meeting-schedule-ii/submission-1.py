"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ti = []
        res,cur=0,0
        for i in intervals:
            ti.append([i.start,1])
            ti.append([i.end,-1])
        ti.sort(key=lambda x: (x[0],x[1]))

        for t in ti:
            if t[1]==1:
                cur+=1
            elif t[1]==-1:
                cur-=1
            res=max(res,cur)
        return res
            