# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        P = deque([p])
        Q = deque([q])

        while P and Q:
            for _ in range(len(P)):
                p = P.popleft()
                q = Q.popleft()
                if p is None and q is None:
                    continue
                if p is None or q is None or p.val != q.val:
                    return False
                
                P.append(p.left)
                P.append(p.right)
                Q.append(q.left)
                Q.append(q.right)
        
        return True