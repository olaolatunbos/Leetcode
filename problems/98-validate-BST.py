# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        output = []
        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)
            output.append(root.val)
            inOrder(root.right)
        inOrder(root)
        # inOrder list should be sorted, therefore we can compare
        return True if output == list(sorted(set(output))) else False