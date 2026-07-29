class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]  # start at 0
        current_sum = 0

        for num in nums:
            if current_sum + num < num:
                # restart subarray at num
                current_sum = num
            else:
                current_sum += num  # add num

            max_sum = max(max_sum, current_sum)

        return max_sum
