# 112. Path Sum
# https://leetcode.com/problems/path-sum

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Recursively checks if any root-to-leaf path sums to targetSum.
        """

        if not root:
            return False  # Empty tree has no path

        # Subtract current node value from target
        targetSum -= root.val

        # If it's a leaf node, check if remaining targetSum is 0
        if not root.left and not root.right:
            return targetSum == 0

        # Recur on left and right subtrees
        return (
            self.hasPathSum(root.left, targetSum) or
            self.hasPathSum(root.right, targetSum)
        )

"""
✅ Time Complexity: O(n)
👉 Must visit each node once in worst case

✅ Space Complexity: O(h)
👉 h = height of the tree (due to recursion stack)
→ O(log n) for balanced, O(n) for skewed tree+

"""
