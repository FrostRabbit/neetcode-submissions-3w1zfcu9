class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1,n2=len(num1),len(num2)
        res = [0]*(n1+n2)

        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                m = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))

                res[i+j+1]+=m
                res[i+j]+=res[i+j+1]//10
                res[i+j+1]%=10
        count=0
        res="".join(str(x) for x in res)
        return res.lstrip('0')

