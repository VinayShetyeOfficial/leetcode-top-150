# 108. Convert Sorted Array to Binary Search Tree (Easy)
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Recursively builds a height-balanced BST from a sorted array.
        Chooses the middle element as root to ensure balance.
        """

        def buildBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # Recursively build left and right subtrees
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)

            return root

        return buildBST(0, len(nums) - 1)

"""
✅ Time Complexity: O(n)
👉 Each element in nums is visited once to build the tree.

✅ Space Complexity: O(log n)
👉 Recursive call stack height = height of the tree = log n (balanced)
"""