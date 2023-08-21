class Solution(object):
    def kthSmallest(self, root, k):
        # heap version
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        heap = []
        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)
            heapq.heappush(heap, root.val)
            inOrder(root.right)
        

        inOrder(root)
        for i in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)