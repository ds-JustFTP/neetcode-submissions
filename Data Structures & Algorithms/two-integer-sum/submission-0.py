class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

sol = Solution()
print(sol.twoSum(nums = [3,4,5,6], target = 7))   
print(sol.twoSum(nums = [4,5,6], target = 10))