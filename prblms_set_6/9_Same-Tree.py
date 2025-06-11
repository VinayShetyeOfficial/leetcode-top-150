# 100. Same Tree (Easy)
# https://leetcode.com/problems/same-tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Recursively checks if two binary trees are structurally identical
        and have the same node values.
        """
        # Both nodes are None → trees match at this branch
        if not p and not q:
            return True

        # One node is None or values mismatch → trees differ
        if not p or not q or p.val != q.val:
            return False

        # Recurse on left and right subtrees
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )

"""
✅ Time Complexity: O(n)
👉 Each node is visited once

✅ Space Complexity: O(h)
👉 h = height of the tree (recursion stack)
→ O(log n) for balanced, O(n) for skewed
"""