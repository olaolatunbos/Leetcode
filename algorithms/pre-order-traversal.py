class Solution:
    def preOrderTraversal(self, root):
        res = []

        def preOrder(root):
            if not root:
                return
            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        return res