class Solution:
    def isHappy(self, n: int) -> bool:
        m ={}
        while n != 1:
            s=0
            while n:
                s+=(n%10)**2
                n//=10
            if s in m:
                return False
            n=s
            m[n]=1
            
        return True