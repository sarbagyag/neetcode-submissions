# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0 # initializing the global variable which will contain answer

        def dfs(root):
            nonlocal res # non local aka global

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right) # comparing global variable with the sum of left and right subtree at each node

            return 1 + max(left, right) # this returns the depth of each node 

        dfs(root)
        
        return res

        
