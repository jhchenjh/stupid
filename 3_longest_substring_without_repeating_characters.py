# 23 Jan, 2020
# Runtime: 108 ms, faster than 18.12% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 12.7 MB, less than 32.03% of Python online submissions for Longest Substring Without Repeating Characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        start = 0
        exit_char = {}
        for i in range(len(s)):
            if s[i] in exit_char.keys():
                start = max(start, exit_char[s[i]] + 1)
            exit_char[s[i]] = i
            result = max(result, i - start + 1)
        return result
