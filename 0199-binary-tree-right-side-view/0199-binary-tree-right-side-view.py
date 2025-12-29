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

        result = [root.val]
        q = deque([root.left, root.right])

        while q:
            for i in range(0, len(q)):
                if q[i]:
                    print(q[i].val, end=" ")
            print()

            count = len(q)
            right = None
            while count > 0:
                node = q[0]
                q.popleft()
                count -= 1

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    right = node.val
                
                if count == 0 and right is not None:
                    result.append(right)

        return result
                

            
        
           