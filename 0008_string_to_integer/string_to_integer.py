class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN: int = -(2**31)  # -2^(n-1)
        INT_MAX: int = 2**31 - 1  # 2^(n-1) - 1

        s = s.strip()  # get rid of trailing whitespaces
        is_negative: bool = False
        num = 0

        if s and s[0] in ["+", "-"]:
            # check if negative and strip
            is_negative = s[0] == "-"
            s = s[1::]

        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + int(c)  # basic base-10 logic

        # Handle the 32-bit signed rounding
        num = -num if is_negative else num
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        return num
