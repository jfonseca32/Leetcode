class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1

        while end > start:
            if (a := min(height[start], height[end]) * (end - start)) > max_area:
                max_area = a

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_area
