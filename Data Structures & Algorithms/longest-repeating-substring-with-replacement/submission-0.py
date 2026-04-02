class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l =0
        m ={}
        res = 0
        maxf=0
        for i in range(len(s)):
            m[s[i]] = 1+ m.get(s[i],0)
            maxf=max(maxf,m[s[i]])
            if (i-l+1)-maxf > k:
                m[s[l]] -=1
                l += 1
            res = max(res,i-l+1)
        return res