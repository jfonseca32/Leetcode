class Solution:
    def isValid(self, s: str) -> bool:
        brackets: dict[str, str] = {
            "{": "}",
            "(": ")",
            "[": "]",
        }

        stack: list[str] = []
        for c in s:
            if c in brackets:
                # opening brackets append
                stack.append(c)
            else:
                if not stack:
                    # closing bracket alone
                    return False

                previous: str = stack.pop()
                if brackets[previous] != c:
                    # closing bracket not matching previous opening
                    return False

        return not stack  # stack empty means all brackets acccounted
