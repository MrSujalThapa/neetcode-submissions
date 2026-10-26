class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        pass
        found = True

        for word in words:
            left = 0
            right = len(word) - 1
            
            while left < right:
                if word[left] == word[right]:
                    found = True
                    right -= 1
                    left += 1
                else:
                    found = False
                    break
            if found:
                return word
        return ""

        
            

