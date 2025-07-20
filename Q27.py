# Largest Rectangle In Histogram
# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

# Return the area of the largest rectangle that can be formed among the bars.

# Note: This chart is known as a histogram.

# heights = [2, 1, 5, 6, 2, 3]
heights = [7,1,7,2,2,4]

class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # Append a zero height to pop all remaining bars

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
Solution = Solution()
print(Solution.largestRectangleArea(heights))  # Output: 8    