class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, curr_combination, target):
            if target == 0:
                result.append(list(curr_combination))
                return
            
            if target < 0:
                return
            
            for num in range(index, len(nums)):
                curr_combination.append(nums[num])
                backtrack(num, curr_combination, target - nums[num])
                curr_combination.pop()
            
        backtrack(0, [], target)
        return result
            