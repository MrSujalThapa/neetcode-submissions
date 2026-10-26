class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        output = 0
        left = 0
        sums = sum(nums[:k])

        for right in range(k -1, len(arr)):
            sums - nums[left] + nums[right]
            if sums//k >= threshold:
                output +=1
            
            left += 1
        return output

