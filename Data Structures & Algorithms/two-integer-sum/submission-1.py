class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = set()
        for i, val in enumerate(nums):
            if ((target - val) in nums):
                return [nums.index(target - val), i]
            nums2.add(val)