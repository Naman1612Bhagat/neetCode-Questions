# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = sorted(s)
        second = sorted(t)
        return first == second