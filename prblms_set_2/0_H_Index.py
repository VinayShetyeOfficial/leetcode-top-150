# 274. H-Index (Medium) - Done
# https://leetcode.com/problems/h-index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Returns the researcher's H-index.
        H-index is the maximum value h such that the researcher has published
        at least h papers that have each been cited at least h times.
        """

        # Step 1: Sort citations in descending order
        citations.sort(reverse=True)

        h_index = 0  # Track the maximum h-index found

        # Step 2: Iterate over sorted citations
        for paper_index, citation_count in enumerate(citations):
            if citation_count >= paper_index + 1:
                h_index += 1
            else:
                break  # Once citation < position, condition fails

        return h_index


"""
✅ Time Complexity: O(n log n)
👉 Sorting takes O(n log n), traversal is O(n)

✅ Space Complexity: O(1)
👉 Sorting is in-place (Python’s built-in `sort`), and we use constant extra variables.
"""

