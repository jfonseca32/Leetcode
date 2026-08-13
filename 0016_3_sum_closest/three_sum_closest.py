class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()  # need monotonic to search efficiently
        smallest = nums[0] + nums[1] + nums[2]
        i = 0

        while i < (len(nums) - 2):  # i > left > right
            left = i + 1  # all nums before i were already checked
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # update smallest
                if abs(total - target) < abs(smallest - target):
                    smallest = total

                if total > target:
                    right -= 1  # need smaller total
                elif total < target:
                    left += 1  # need bigger total
                else:
                    return smallest  # perfect hit, return

            i += 1

        return smallest
