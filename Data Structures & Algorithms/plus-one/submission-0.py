class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        flag=True
        for i in range(len(digits)-1,-1,-1):
            if flag:
                digits[i]+=1
                flag=False  
            if digits[i] == 10:
                digits[i]=0
                flag=True
        
        return [1] + digits if flag else digits
