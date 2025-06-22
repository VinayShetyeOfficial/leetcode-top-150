# 637. Average of Levels in Binary Tree (Easy)
# https://leetcode.com/problems/average-of-levels-in-binary-tree

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Returns the average of nodes' values on each level of the binary tree.
        Uses BFS to traverse level-by-level.
        """

        result = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result

"""
✅ Time Complexity: O(n)
👉 Each node is visited once

✅ Space Complexity: O(w)
👉 `w` is the max width of the tree (max number of nodes at any level)
"""
