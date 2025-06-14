# 222. Count Complete Tree Nodes (Easy) - Done
# https://leetcode.com/problems/count-complete-tree-nodes

from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Counts the total number of nodes in a binary tree using BFS.
        Traverses level by level and increments count for each node.
        """

        if not root:
            return 0

        count = 1
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                count += 1

            if node.right:
                queue.append(node.right)
                count += 1

        return count

"""
✅ Time Complexity: O(n)
👉 Visits each node once

✅ Space Complexity: O(w)
👉 `w` is the maximum width of the tree (worst case for a full level)
"""