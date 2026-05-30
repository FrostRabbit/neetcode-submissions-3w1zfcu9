class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def DFS(i,s):
            if i == len(digits):
                res.append(s)
                return
            
            for c in m[digits[i]]:
                DFS(i+1,s+c)
        
        if digits:
            DFS(0,"")
        
        return res