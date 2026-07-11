class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, curr_subset):
            result.append(list(curr_subset))
            for i in range(index, len(nums)):
                curr_subset.append(nums[i])
                backtrack(i + 1, curr_subset)
                curr_subset.pop()

        backtrack(0, [])
        return result
                