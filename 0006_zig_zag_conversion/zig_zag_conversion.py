class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # edge case; output is just s
        if numRows == 1:
            return s

        h = 2 * numRows - 2  # size of each "cycle"
        buckets = [""] * numRows

        for i, c in enumerate(s):
            val = i % h  # separates into correct bucket

            # when it is coming back (val >= numRows), we start from h instead of 0
            bucket = val if val < numRows else h - val
            buckets[bucket] += c

        return "".join(buckets)
