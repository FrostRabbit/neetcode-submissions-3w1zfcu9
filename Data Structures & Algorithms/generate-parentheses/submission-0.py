class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def dfs(leftN,rightN):
            if leftN==rightN==n:
                res.append("".join(cur))
            
            if leftN < n:
                cur.append("(")
                dfs(leftN+1,rightN)
                cur.pop()
            if rightN < leftN:
                cur.append(")")
                dfs(leftN,rightN+1)
                cur.pop()
        dfs(0,0)
        return res