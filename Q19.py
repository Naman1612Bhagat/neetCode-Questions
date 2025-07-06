# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        left = 0
        right = 0
        min_length = float('inf')
        min_window = ""
        window_count = {}
        while right < len(s):
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            while all(window_count.get(char, 0) >= t_count.get(char, 0) for char in t_count):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right+1]
                window_count[s[left]] -= 1
                left += 1
            right += 1
        return min_window
    
    