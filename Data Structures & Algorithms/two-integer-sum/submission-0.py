class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num_to_index = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen_num_to_index:
                return [seen_num_to_index[difference], i]
            seen_num_to_index[num] = i
        