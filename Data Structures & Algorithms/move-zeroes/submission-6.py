class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] != 0:
                left += 1

                # Keep right ahead of left
                if right <= left:
                    right = left + 1

            elif nums[right] == 0:
                right += 1

            else:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1
                right += 1