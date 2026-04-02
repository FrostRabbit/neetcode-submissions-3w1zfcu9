class Solution:
    def reverse(self, x: int) -> int:
        st=""
        num = abs(x)
        sign =0
        if x>0:
            sign = 1
        elif x < 0: 
            sign = -1
        else: return 0
        while num > 0:
            st += str(num%10)
            num = int(num/10)
        if int(st) > 2147483647:return 0
        else: return int(st)*sign