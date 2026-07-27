class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
#lets say we have [1,1,2,2] pair starts at even index ends at odd
#[1,1,2,3,3] 1 and 1 follow this pattern but 3 and 3 starts at odd and ends at even
#[1,1,2,3,3,4,4,8,8] middle is 4 originally which is 3 now 3 is at index 4 which means 
#it's pair should be at 5 but since it's pair is at index 3 we know that the prob element
#is before this middle

        left = 0
        right = len(nums) - 1
        before = False
        if right == 0:
            return nums[left]

        while left < right:
            middle = (left + right) // 2
            if middle == 0:
                return nums[middle]

            if middle % 2 == 0:
                if nums[middle] == nums[middle + 1]:
                    left = middle + 1
                elif nums[middle] != nums[middle - 1]:
                    return nums[middle]
                else:
                    right = middle - 1
                    
            if middle % 2 != 0:
                if nums[middle] == nums[middle - 1]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return nums[left]