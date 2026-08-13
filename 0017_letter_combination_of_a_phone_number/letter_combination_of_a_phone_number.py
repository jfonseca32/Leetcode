class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone: dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int, combination: str):
            if index == len(digits):  # base case
                # this combination a letter of every digit
                result.append(combination)
                return

            for letter in phone[digits[index]]:
                # not at end of digits
                # recurse for every letter in this depth; go an index deeper
                backtrack(index + 1, combination + letter)

        result: list[str] = []
        backtrack(0, "")
        return result
