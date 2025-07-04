# 104. Maximum Depth of Binary Tree (Easy) - Done
# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursion Approach
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


"""
✅ Time Complexity: O(n)
👉 Every node is visited once

✅ Space Complexity: O(h)
👉 h = height of tree = recursion stack depth
👉 Worst case: O(n) for skewed tree, O(log n) for balanced tree
"""
    
#--------------------------------------------------------------------------
# Alternative Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS Approach
        if not root:
            return 0
        
        level = 0
        q = deque([root])

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level += 1
        return level

"""
✅ Time Complexity: O(n)
👉 Each node is processed once

✅ Space Complexity: O(w)
👉 w = maximum width of the tree (number of nodes at the widest level)
👉 Worst case: O(n) for a full binary tree (last level has ~n/2 nodes)
"""

#--------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS Approach
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
    
"""
✅ Time Complexity: O(n)
👉 Every node is visited once

✅ Space Complexity: O(h)
👉 h = max height of the tree = max stack size
👉 Worst case: O(n) for skewed tree, O(log n) for balanced tree
"""
    