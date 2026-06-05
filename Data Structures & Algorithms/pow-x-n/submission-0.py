class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1.0
        p = abs(n)
        while p:
            if p%2==1:
                res*=x
            x*=x
            p//=2
        return res if n>=0 else 1/res