# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        q = deque([root])

        while q:
            result.append(q[-1].val)

            count = len(q)
            while count > 0:
                node = q[0]
                q.popleft()
                count -= 1

                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        return result
                

            
        
           