class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for i, num in enumerate(nums):
            ans.append(num)
        return ans