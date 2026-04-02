class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st+= str(len(s)) + "#" + s
        return st
    def decode(self, s: str) -> List[str]:
        result = []
        st = ""
        start = 0
        while start < len(s):
            end = start
            while s[end] != '#':
                end += 1
            num = int(s[start:end])
            start = end +1
            end = start + num
            result.append(s[start:end])
            start = end
        return result
