# Median of Two Sorted Arrays
# Solved 
# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in O(log(m+n)) time.

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        arr = nums1 + nums2
        sorted_arr = sorted(arr)

        n = len(arr)

        if n % 2 == 0:
            mid1 = sorted_arr[n // 2 - 1]
            mid2 = sorted_arr[n // 2]
            med = (mid1 + mid2)/2
        else:
            med = sorted_arr[n // 2]    
        return med