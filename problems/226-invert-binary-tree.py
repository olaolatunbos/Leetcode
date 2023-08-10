class Solution:
    def invertTree(self, root):
        # base case
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root