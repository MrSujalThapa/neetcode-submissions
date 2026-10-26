class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = {}

        for i in range(len(s)):
            if s[i] not in maps:
                maps[s[i]] = t[i]
            else:
                if maps[s[i]] != t[i]:
                    return False

        return True