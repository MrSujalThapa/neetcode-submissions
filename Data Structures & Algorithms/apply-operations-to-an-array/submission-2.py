class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        pass

        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] = nums[left] + nums[right]
                nums[right] = 0
            right += 1
            left += 1
        
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == 0:
                if nums[right] != 0:
                    nums[left] = nums[right]
                    nums[right] = 0
                    left += 1
            else:
                left += 1
            right += 1
        return nums
