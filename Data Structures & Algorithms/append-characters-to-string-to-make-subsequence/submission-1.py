class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #s = "coaching", t = "coding"
        #s="abcde" t="a"
        left = 0

        for char in s:
            if left < len(t) and char == t[left]:
                left += 1
        
        return len(t) - left