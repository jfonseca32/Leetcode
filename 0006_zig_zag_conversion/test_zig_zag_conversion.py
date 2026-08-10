import pytest
from zig_zag_conversion import Solution


@pytest.mark.parametrize(
    "s, numRows, expected",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ],
)
class TestZigZagConversion:
    def test_zig_zag_conversion(self, s: str, numRows: int, expected: str):
        result = Solution().convert(s, numRows)

        assert result == expected
