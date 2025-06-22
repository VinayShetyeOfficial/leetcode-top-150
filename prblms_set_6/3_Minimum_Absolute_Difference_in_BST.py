# 530. Minimum Absolute Difference in BST (Easy)
# https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Performs in-order traversal of the BST to get nodes in sorted order.
        Tracks and returns the minimum difference between adjacent nodes.
        """

        prev_node = None
        min_diff = float('inf')

        def in_order(node: Optional[TreeNode]):
            nonlocal prev_node, min_diff
            if not node:
                return

            # Traverse left subtree
            in_order(node.left)

            # Update minimum difference
            if prev_node is not None:
                min_diff = min(min_diff, node.val - prev_node.val)
            prev_node = node

            # Traverse right subtree
            in_order(node.right)

        in_order(root)
        return min_diff


"""

"""