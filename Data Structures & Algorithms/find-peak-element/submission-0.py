class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle + 1] > nums[middle]:
                left = middle + 1
            
            elif nums[middle + 1] < nums[middle]:
                right = middle
        
        return left