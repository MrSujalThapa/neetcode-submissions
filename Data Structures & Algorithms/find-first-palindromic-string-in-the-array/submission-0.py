class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        pass

        left = 0
        found = False

        for word in words:
            if len(word) == 1:
                return word
            right = len(word) - 1
            while left < right:
                if word[left] == word[right]:
                    right -= 1
                    left += 1
                    found = True
                else:
                    found = False
                    break
            if found:
                return word
        return ""

        
            

