class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pass
        b4 = []
        piv = []
        after = []

        for num in nums:
            if num < pivot:
                b4.append(num)
            elif num == pivot:
                piv.append(num)
            else:
                after.append(num)
        return b4 + piv + after
