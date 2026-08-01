class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        minu = 0

        
        if k == 1:
            return 0
        nums.sort()
        left = 0
        
        minu = nums[k-1] - nums[left]

        for right in range(k-1, len(nums)):

            tempMin = nums[right] - nums[left]
            minu = min(tempMin, minu)
            left += 1
        return minu
            