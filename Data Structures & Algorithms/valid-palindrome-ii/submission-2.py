class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        hasDeletedOne = False

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() == s[right].lower():
                left += 1
                right -=1
            elif not hasDeletedOne and s[left].lower() != s[right].lower():
                if s[left + 1].lower() == s[right].lower():
                    left += 1
                elif s[right - 1].lower() == s[left].lower():
                    right -= 1
                else:
                    return False
                hasDeletedOne = True
            else:
                return False
        
        return True


 
