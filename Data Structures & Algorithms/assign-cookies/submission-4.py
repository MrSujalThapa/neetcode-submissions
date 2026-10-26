class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left = 0
        k = 0
        right = 0
        s.sort()
        g.sort()

        while right < len(s) and left < len(g):
            if g[left] <= s[right]:
                left += 1
                k += 1
                continue
            right += 1
        
        return k
            
