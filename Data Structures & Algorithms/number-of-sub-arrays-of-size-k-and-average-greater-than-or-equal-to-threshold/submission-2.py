class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        output = 0
        left = 0
        sums = sum(arr[:k])
        if sums//k >= threshold:
                output = 1

        for right in range(k, len(arr)):
            sums = sums - arr[left] + arr[right]
            if sums//k >= threshold:
                output +=1
            
            left += 1
        return output

