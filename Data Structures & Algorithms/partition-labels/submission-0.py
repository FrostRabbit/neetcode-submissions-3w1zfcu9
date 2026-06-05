class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        k = 0
        k1= 0
        res=[]
        for i in s:
            k1+=1
            if count[i]:
                k+=count[i]
                count[i]=0
            if k==k1:
                res.append(k1)
                k1=0
                k=0
        return res
