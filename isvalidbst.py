# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []

        def inorder(root):

            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)

        if res:
            if len(res) == 1:
                return True
            inc = 0
            for ele in res[1:]:
                if ele <= res[inc]:
                    return False
                inc += 1
            return True

        return False


sol = Solution()
