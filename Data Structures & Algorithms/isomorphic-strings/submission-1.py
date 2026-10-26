class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {} # {a: b, b: d}...
        i = 0
        isomorphic = True
        for i, letter in enumerate(s):
            if letter in map:
                if map[letter] != t[i]:
                    isomorphic = False
                    break
                else:
                    continue
            map[letter] = t[i]
            i += 1
        
        return (isomorphic and i == len(map))