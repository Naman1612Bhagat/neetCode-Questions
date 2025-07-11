# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagram[key].append(word)
        
        return list(anagram.values())