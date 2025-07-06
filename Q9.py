# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_length = 0
        current_length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            elif nums[i] != nums[i-1]:
                max_length = max(max_length, current_length)
                current_length = 1
            else:
                return 0    
        return max(max_length, current_length)
    