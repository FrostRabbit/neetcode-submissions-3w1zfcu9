class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n
        def dfs(path):
            if len(path) == n:
                res.append(path.copy())
                return
            
            for i in range(n):
                if used[i] == True:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(path)
                path.pop()
                used[i] = False
        dfs([])
        return res