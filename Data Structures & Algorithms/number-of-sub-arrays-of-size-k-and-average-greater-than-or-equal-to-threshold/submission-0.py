class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        output = 0
        left = 0

        for right in range(k -1, len(arr)):
            if sum(arr[left:right + 1])//k >= threshold:
                output += 1
            
            left += 1
        return output

