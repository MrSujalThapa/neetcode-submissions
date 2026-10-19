class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pass
        
        output1 = []
        output2 = []

        left = 0
        for right in range(len(s)):
            if len(output1) > 0 and s[right] == "#":
                output1.pop()
            elif s[right] != "#":
                output1.append(s[right])
        
        for left in range(len(t)):
            if len(output2) > 0 and t[left] == "#":
                output2.pop()
            elif t[left] != "#":
                output2.append(t[left])

        return output1 == output2
        



