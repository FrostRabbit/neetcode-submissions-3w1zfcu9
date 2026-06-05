class Solution:
    def isHappy(self, n: int) -> bool:
        m =set()
        while n != 1:
            s=0
            while n:
                s+=(n%10)**2
                n//=10
            if s in m:
                return False
            n=s
            m.add(n)
            
        return True