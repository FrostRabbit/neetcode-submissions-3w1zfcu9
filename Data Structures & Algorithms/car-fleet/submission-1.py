class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pa = [(p,s) for p,s in zip(position, speed)]
        pa.sort(reverse=True)
        res=1
        pre = (target-pa[0][0])/pa[0][1]
        for i in range(1,len(position)):
            cur = pa[i]
            dif = (target-cur[0])/cur[1]
            if  dif> pre:
                res+=1
                pre = dif
        return res