class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_ind = {}
        first_ind = largest = 0

        for ind, char in enumerate(s):
            if char in char_to_ind and char_to_ind[char] >= first_ind:
                first_ind = char_to_ind[char] + 1

            largest = max(ind - first_ind + 1, largest)
            char_to_ind[char] = ind

        return largest
