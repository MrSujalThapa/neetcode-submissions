class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #run through loop --> bruteforce
        #create a set and add each value to the set

        copy = set()
        for num in nums:
            if num in copy:
                return True
            copy.add(num)
        return False