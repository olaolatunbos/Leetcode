class Solution:
    def inOrderTraversal(self, root):
        res = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.left) 
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return res