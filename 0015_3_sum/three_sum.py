class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # sort for monotonicity
        three_sum: list[list[int]] = []
        i = 0

        while i < len(nums) - 2:  # i > left > right
            if nums[i] > 0:  # i is smallest; no way to get to 0
                break

            while i > 0 and i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1  # skip duplicates
                continue

            left = i + 1  # left > i; already checked all left of i
            right = len(nums) - 1  # right > left

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1  # need greater number
                elif total > 0:
                    right -= 1  # need smaller number
                else:
                    # hit; add and advance
                    three_sum.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

            i += 1

        return three_sum
