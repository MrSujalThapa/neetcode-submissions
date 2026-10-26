class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pass
        left = 0
        right = 0

        while left < len(nums1) or right < len(nums2):
            if left < len(nums1) and right > len(nums2):
                output.append(nums1[left][0], nums1[left][1])
                continue
            if left > len(nums1) and right < len(nums2):
                output.append(nums2[left][0], nums2[left][1])
                continue
        
            val1 = nums1[left][1]
            val2 = nums1[right][1]
            id1 = nums1[left][0]
            id2 = nums2[right][0]
            if id1 < id2:
                output.append(nums1[left])
                right += 1
            elif id1 == id2:
                output.append(id1, val1 + val2)
                right += 1
                left += 1
            else:
                output.append(nums1[right])
                left += 1
        
        return output