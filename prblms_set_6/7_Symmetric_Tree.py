# 101. Symmetric Tree (Easy) - Done
# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val and 
                    dfs(left.left, right.right) and
                    dfs(left.right, right.left))
        return dfs(root.left, root.right)
        

"""
✅ Time Complexity: O(n)
👉 Each node is visited once

✅ Space Complexity: O(h)
👉 h = height of tree, for recursion stack
→ O(log n) for balanced, O(n) for skewed
"""

