# 26 Jan, 2020
# Runtime: 5224 ms, faster than 14.39% of Python online submissions for Longest Palindromic Substring.
# Memory Usage: 20.3 MB, less than 24.66% of Python online submissions for Longest Palindromic Substring.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        dp_table = [[0 for x in range(size)] for y in range(size)]

        max_length = 1
        i = 0
        while (i < size) :
            dp_table[i][i] = True
            i = i + 1

        start = 0
        i = 0
        while i < size - 1:
            if (s[i] == s[i + 1]) :
                dp_table[i][i + 1] = True
                start = i
                max_length = 2
            i = i + 1

        k = 3
        while k <= size:
            i = 0
            while i < (size - k + 1):
                j = i + k - 1
                if (dp_table[i + 1][j - 1] and s[i] == s[j]):
                    dp_table[i][j] = True
                    if (k > max_length):
                        start = i
                        max_length = k
                i = i + 1
            k = k + 1

        return s[start:start+max_length]
