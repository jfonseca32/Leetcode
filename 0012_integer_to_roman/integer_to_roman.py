class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""

        # Max number is 3999, so this logic works
        int_to_roman: dict[int, tuple[str, ...]] = {
            1: ("I", "X", "C", "M"),
            5: ("V", "L", "D"),
        }  # Could make a bigger dict with 1000, 900, 500, etc. for faster runtime but greater mem

        count = (
            0  # To signal which decimal place and consequently which index of the tuple
        )
        while num > 0:
            smallest = num % 10  # last digit

            # Conversion logic (built in reverse so O(1) amortized)
            if smallest < 4:
                roman = roman + smallest * int_to_roman[1][count]
            elif smallest == 4:
                roman = roman + int_to_roman[5][count] + int_to_roman[1][count]
            elif smallest == 5:
                roman = roman + int_to_roman[5][count]
            elif smallest > 5 and smallest < 9:
                roman = (
                    roman
                    + (smallest - 5) * int_to_roman[1][count]
                    + int_to_roman[5][count]
                )
            elif smallest == 9:
                roman = roman + int_to_roman[1][count + 1] + int_to_roman[1][count]

            count += 1
            num //= 10  # remove last digit

        return roman[::-1]  # reverse back
