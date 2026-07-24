class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        write = 0
        output = []
        if len(nums) == 1:
            return nums

        while left <= right:
            if nums[left] % 2 == 0:
                output.append(nums[left])
                left += 1
            elif nums[right] %2 == 0:
                output.append(nums[right])
                right -= 1
            else:
                right -= 1
        
        if len(output) != len(nums):
            for i in range(left, len(nums)):
                if nums[i] % 2 != 0:
                    output.append(nums[i])

            
        return output

        