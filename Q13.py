# You are given an integer array heights where heights[i] represents the height of the ith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            current_area = min(heights[i], heights[j]) * (j - i)
            max_area = max(max_area, current_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area