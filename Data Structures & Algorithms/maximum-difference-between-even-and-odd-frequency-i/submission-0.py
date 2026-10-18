class Solution:
    def maxDifference(self, s: str) -> int:
        maxi = 0
        mini = 100
        maps = {}
        
        for char in s:
            maps[char] = maps.get(char, 0) + 1
        
        for val in maps:
            if maps[val] % 2 == 0:
                mini = min(mini, maps[val])
            else:
                maxi = max(maxi, maps[val])
        
        return maxi - mini

