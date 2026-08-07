class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        long = ""

        for i in range(len(strs[0])):
            if all(i < len(word) and word[i] == strs[0][i] for word in strs):
                long += strs[0][i]
                continue
            else:
                break

        return long
