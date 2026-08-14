class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()  # sort for monotonicity
        result: list[list[int]] = []

        for i in range(len(nums) - 3):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(len(nums) - 1, i + 2, -1):
                # skip duplicates
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    continue

                left = i + 1
                right = j - 1  # i < left < right < j

                while left < right:
                    total = nums[i] + nums[left] + nums[right] + nums[j]

                    if total > target:
                        right -= 1  # need to decrease total
                    elif total < target:
                        left += 1  # need to increase total
                    else:
                        result.append([nums[i], nums[left], nums[right], nums[j]])
                        left += 1
                        right -= 1  # append and advance inner pointers

                        # skip duplicates
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return result
