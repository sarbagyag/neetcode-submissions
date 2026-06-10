# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        deq = collections.deque()

        deq.append(root)
 
        while deq:
            innerRes = []
            lendeq = len(deq)
            for i in range(lendeq):
                node = deq.popleft()
                if node:
                    innerRes.append(node.val)
                    deq.append(node.left)
                    deq.append(node.right)
                
            if innerRes:
                res.append(innerRes)
        
        return res

            

            
        
        