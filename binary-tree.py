# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    




# #LEFT, ROOT, RIGHT
# def inOrderTraversal(root):
#     res = []

#     def inOrder(root):
#         if not root:
#             return
#         inOrder(root.left) # finishes when we reach a node of None, as returns None
#         res.append(root.val)
#         inOrder(root.right)

#     inOrder(root)
#     return res

# #ROOT, LEFT, RIGHT
# def preOrderTraversal(root):
#     res = []

#     def preOrder(root):
#         if not root:
#             return
#         res.append(root.val)
#         preOrder(root.left)
#         preOrder(root.right)

#     preOrder(root)
#     return res

# #LEFT, RIGHT, ROOT
# def postOrderTraversal(root):
#     res = []

#     def postOrder(root):
#         if not root:
#             return
#         postOrder(root.left)
#         postOrder(root.right)
#         res.append(root.val)

#     postOrder(root)
#     return res

# def maxDepth(root):
#     if not root:
#         return 0
    
#     return 1 + max(maxDepth(root.left), maxDepth(root.right))



# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)

# node1.left = node2
# node1.right = node3
# print(maxDepth(node1))

# print(inOrder(node1))
# print(preOrderTraversal(node1))
# print(postOrderTraversal(node1))


a = "-10"
b = "5"

stack = [1,4,3]

stack.sort()
print(stack)