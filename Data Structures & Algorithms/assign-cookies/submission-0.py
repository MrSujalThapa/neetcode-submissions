class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left = len(g) -1
        if not s:
            return 0
        right = len(s) - 1
        k = 0

        while 0 <= left and 0 <= right:
            if s[right] < g[left]:
                left -= 1
            elif s[right] >= g[left]:
                k += 1
                left -= 1
                right -= 1
        
        return k
                