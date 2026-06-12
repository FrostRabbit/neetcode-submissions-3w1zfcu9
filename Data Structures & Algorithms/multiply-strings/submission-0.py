class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2=len(num1)-1,len(num2)-1
        s1,s2=0,0
        for i in range(n1,-1,-1):
            s1+=(10**(n1-i))*(ord(num1[i])-ord('0'))

        for i in range(n2,-1,-1):
            s2+=(10**(n2-i))*(ord(num2[i])-ord('0'))
        
        return str(s1*s2)