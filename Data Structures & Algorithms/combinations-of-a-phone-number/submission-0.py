class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
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

        res = [""]

        for d in digits:
            temp=[]
            for r in res:
                for c in m[d]:
                    temp.append(r+c)
            res = temp
        return res
