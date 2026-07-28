class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hashmap for O(N) time and space
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num  # get number to check dict

            if complement in num_to_index:  # check if complement in dict
                return [num_to_index[complement], i]

            num_to_index[num] = i  # add num-index to dict

        raise ValueError("No two sum solution")
