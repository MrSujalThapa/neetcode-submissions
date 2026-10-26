class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        hasDeletedOne = False

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right += 1
            
            if s[left] == s[right]:
                left += 1
                right -=1

            elif not hasDeletedOne and s[left] != s[right]:
                if s[left + 1] == s[right]:
                    left += 1
                elif s[right - 1] == s[left]:
                    right -= 1
                else:
                    return False
                hasDeletedOne = True
            else:
                return False
        
        return True


 
