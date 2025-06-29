# 226. Invert Binary Tree (Easy) - Done
# https://leetcode.com/problems/invert-binary-tree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursively inverts a binary tree by swapping left and right subtrees.
        """

        if not root:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Recurse on children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

"""
✅ Time Complexity: O(n)
👉 Must visit every node once to swap children

✅ Space Complexity: O(h)
👉 h = height of tree (recursion stack)
→ O(log n) for balanced, O(n) for skewed
"""

# Alternate Solution
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left  # swap children

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
