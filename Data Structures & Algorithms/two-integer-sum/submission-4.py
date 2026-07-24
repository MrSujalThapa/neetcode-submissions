class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      info = {}
      required = 0
      for i, value in enumerate(nums):
        required = target - value
        if required in info:
            return [info[required], i]
        info[value] = i