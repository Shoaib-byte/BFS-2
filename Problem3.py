# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root.left,root.right])
        if root == None:
            return True
    
        while q:
            left = q.popleft()
            right = q.popleft()
            if left == None and right == None:
                continue
            if left == None or right == None or left.val != right.val:
                return False
            q.append(left.left)
            q.append(right.right)

            q.append(left.right)
            q.append(right.left)
        
        return True
        