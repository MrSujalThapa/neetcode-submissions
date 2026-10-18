class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        dic = {}
        val = 0

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] >= len(nums)/2:
                return num