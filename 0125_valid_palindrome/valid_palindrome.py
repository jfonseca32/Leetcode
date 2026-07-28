"""
Instead of pointers + while loop, could use reversal too
return cleaned == cleaned[::-1]
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # All lowercase; no special chars
        cleaned = [char.lower() for char in s if char.isalnum()]

        i = 0  # first index pointer
        j = len(cleaned) - 1  # last index pointer

        while i < j:
            if cleaned[i] != cleaned[j]:
                return False

            # Same, move inward
            i += 1
            j -= 1

        return True
