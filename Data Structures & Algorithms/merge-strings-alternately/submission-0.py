class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        left = 0
        right = 0
        while left < len(word1) and right < len(word2):
            output += word1[left] + word2[right]
            left += 1
            right += 1
        
        if len(word1) < len(word2):
            output += word2[right:]
        elif len(word1) > len(word2):
            output += word1[left:]
        
        return output

