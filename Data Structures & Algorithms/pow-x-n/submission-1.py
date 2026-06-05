class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:return 0
        if n==0:return 1
        res=1.0
        p = abs(n)
        while p:
            if p%2==1:
                res*=x
            x*=x
            p//=2
        return res if n>=0 else 1/res