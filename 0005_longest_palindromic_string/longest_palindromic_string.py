class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]

        for i in range(len(s)):
            start1, end1 = self.expand(s, i, i)
            start2, end2 = self.expand(s, i, i + 1)

            if (end1 - start1) > (len(longest) - 1):
                longest = s[start1 : end1 + 1]
            if (end2 - start2) > (len(longest) - 1):
                longest = s[start2 : end2 + 1]

        return longest

    def expand(self, s: str, start: int, end: int) -> (int, int):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        return (start + 1, end - 1)
