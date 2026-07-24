class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        inRow = 0
        finalMax = 0
        i = 0
        while(i < len(nums)):
            if (nums[i] == 1):
                inRow +=1
            else:
                inRow = 0
            finalMax = max(finalMax, inRow)
            i +=1
        return finalMax