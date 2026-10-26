class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = {}
        maps2 = {}

        for i in range(len(s)):
            if s[i] not in maps:
                maps[s[i]] = t[i]
                maps2[t[i]] = s[i]
            else:
                if maps[s[i]] != t[i]:
                    return False
                if maps2[t[i]] != s[i]:
                    return False

        return True