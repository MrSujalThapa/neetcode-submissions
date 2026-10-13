class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #nums=[1,1,0,1,1,1]
        maxi = 0
        one = False
        count = 0
        for num in nums:
            if num == 1:
               count += 1
               one = False
            if num == 0:
                maxi = max(count, maxi)
                count = 0
        
        return max(count, maxi)