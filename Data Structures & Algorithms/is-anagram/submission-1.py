class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}

        for i in s:
            s1[i] = s1.get(i, 0) + 1
        for j in t:
            s2[j] = s2.get(j, 0) + 1

        return s1 == s2