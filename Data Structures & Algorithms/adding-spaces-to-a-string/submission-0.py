class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        output = []

        left = 0
        right = 0
        while right < len(s):
            if not left < len(spaces):
                output.append(s[right:])
                break
            if right == spaces[left]:
                    output.append(" ")
                    left += 1
            output.append(s[right])
            right += 1
        
        return "".join(output)

