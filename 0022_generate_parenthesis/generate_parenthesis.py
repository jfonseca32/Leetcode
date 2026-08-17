class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        combinations: list[str] = []

        def backtrack(combination: str, open: int, closed: int):
            if open == n and closed == n:  # base case all brackets added
                combinations.append(combination)
                return

            if open < n:
                backtrack(combination + "(", open + 1, closed)
            if closed < open:
                # can only add closing if it won't make an invalid expression
                backtrack(combination + ")", open, closed + 1)

        backtrack("", 0, 0)
        return combinations
