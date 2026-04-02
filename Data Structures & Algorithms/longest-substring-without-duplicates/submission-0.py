class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        m = {}
        for i in range(len(s)):
            if s[i] in m:
                l = max(m[s[i]]+1,l)
            m[s[i]] = i
            res = max(res,i-l+1)
        return res