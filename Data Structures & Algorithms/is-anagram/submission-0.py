class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #an anagram has the same characters but diff order
        #create a dictionary to see frequency of letter and if dictionaries match
        s2 = {}
        t2 = {}

        for value in s:
            s2[value] = s2.get(value, 0) + 1
        for value in t:
            t2[value] = t2.get(value, 0) + 1
        
        return s2 == t2