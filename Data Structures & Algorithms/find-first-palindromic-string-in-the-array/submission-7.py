class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        pass

        for word in words:
            left = 0
            right = len(word) - 1
            found = True
            
            while left < right:
                if word[left] != word[right]:
                    found = False
                    break

                left += 1
                right -= 1
            
            if found:
                return word
        return ""

        
            

