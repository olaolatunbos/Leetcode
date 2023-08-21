from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bs(root):
    output = []

    queue = deque()
    queue.append(root)

    while queue:
        level = []
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            queue.append(root.left)
            queue.append(root.right)
            level.append(cur_node.val)
        output.append(level)
    return output

node1 = TreeNode()
node2 = TreeNode()
node3 = TreeNode()

node1.left(node2)
node1.right(node2)

print(bs(node1))

