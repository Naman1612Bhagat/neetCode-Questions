# Given an integer array nums and an integer k, return the k most frequent elements within the array.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        for num in set(nums):
            l.append((num, nums.count(num)))
            l.sort(key=lambda x: x[1], reverse=True)
        return [item[0] for item in l[:k]]  