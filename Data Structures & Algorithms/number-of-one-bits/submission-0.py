class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(0,32):
            if n & 1:
                res+=1
            n >>= 1
        return res