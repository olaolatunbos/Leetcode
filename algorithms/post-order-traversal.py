class Solution:
    def postOrderTraversal(self, root):
        res = []

        def postOrder(root):
            if not root:
                return
            postOrder(root.left)
            postOrder(root.right)
            res.append(root.val)

        postOrder(root)
        return res
