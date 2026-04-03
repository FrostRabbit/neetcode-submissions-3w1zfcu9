# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        st = [[root,1]]
        maxd = 0
        while st:
            node, d = st.pop()
            maxd = max(maxd,d)
            if node.left:
                st.append([node.left,d+1])
            if node.right:
                st.append([node.right,d+1])
        return maxd