class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        w = {}
        count = {}
        for i in t:
            count[i] = 1+count.get(i,0)

        have,need = 0,len(count)
        l=0
        res = [-1,-1]
        rlen = len(s) + 1
        for r in range(len(s)):
            w[s[r]] = 1+ w.get(s[r],0)
            if s[r] in count and count[s[r]] == w[s[r]]:
                have += 1
            while have == need:
                if r-l+1<rlen:
                    res = [l,r]
                    rlen = r-l+1
                w[s[l]] -=1
                if s[l] in count and count[s[l]] > w[s[l]]:
                    have-=1
                l +=1
        l,r = res
        return s[l:r+1] if rlen < len(s)+1 else ""
