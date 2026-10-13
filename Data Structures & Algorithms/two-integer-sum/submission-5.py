class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums = [3,4,5,6], target = 7 Output: [0,1]
        dic = {}

        for i, num in enumerate(nums):
          if target - num in dic:
            return [dic[target - num], i]
          
          dic[num] = i



