# Binary Search
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in O(logn) time.

nums = [-1,0,2,4,6,8]
target = 4

class Solution:
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        return -1
    
Solution = Solution()
print(Solution.search(nums, target))    